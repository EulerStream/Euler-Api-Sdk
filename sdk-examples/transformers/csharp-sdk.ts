import { ParsedOperation, SdkTransformer } from './types';

/**
 * Generate C# examples using the EulerStreamApiClient wrapper.
 * C# generated docs do NOT contain code examples, so we synthesize from the signature + params.
 *
 * Target pattern:
 *   using EulerApiSdk;
 *   using EulerApiSdk.Client;
 *
 *   var client = new EulerStreamApiClient(
 *       host => host.AddTokens(new ApiKeyToken("YOUR_API_KEY", ClientUtils.ApiKeyHeader.ApiKey))
 *   );
 *
 *   var result = await client.Webcast.FetchWebcastURLAsync(roomId: "12345");
 */

function resolvePropertyName(apiClassName: string, overrides: Record<string, string>): string {
  if (overrides[apiClassName]) return overrides[apiClassName];
  return apiClassName.replace(/Api$/, '');
}

function buildNamedArgs(params: ParsedOperation['parameters']): string {
  if (params.length === 0) return '';
  const args = params.filter(p => !p.optional).map(p => {
    switch (p.type.toLowerCase()) {
      case 'string': return `${p.name}: "${p.name}_value"`;
      case 'double':
      case 'number': return `${p.name}: 0`;
      case 'bool':
      case 'boolean': return `${p.name}: true`;
      default: return `${p.name}: ${p.name}`;
    }
  });
  if (args.length === 0) {
    // Use first param even if optional
    const p = params[0];
    if (p) {
      args.push(`${p.name}: "${p.name}_value"`);
    }
  }
  return args.join(', ');
}

export const transformer: SdkTransformer = {
  transform(op: ParsedOperation, overrides: Record<string, string>): string {
    const prop = resolvePropertyName(op.apiClassName, overrides);
    const args = buildNamedArgs(op.parameters);

    // C# async methods have Async suffix
    const asyncMethod = `${op.methodName}Async`;

    // Extract return type from signature
    const retMatch = op.signature.match(/^(\S+)\s+\w+/);
    const hasReturn = retMatch && retMatch[1] !== 'void';

    const call = `client.${prop}.${asyncMethod}(${args})`;
    const lines = [
      `using EulerApiSdk;`,
      `using EulerApiSdk.Client;`,
      ``,
      `var client = new EulerStreamApiClient(`,
      `    host => host.AddTokens(new ApiKeyToken("YOUR_API_KEY", ClientUtils.ApiKeyHeader.ApiKey))`,
      `);`,
      ``,
      hasReturn
        ? `var result = await ${call};`
        : `await ${call};`,
    ];

    return lines.join('\n');
  },
};
