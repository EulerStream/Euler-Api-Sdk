import { ParsedOperation, SdkTransformer } from './types';

/**
 * Transform raw openapi-generator Java examples into EulerStreamApiClient wrapper examples.
 *
 * Raw pattern:
 *   ApiClient defaultClient = Configuration.getDefaultApiClient();
 *   ...
 *   TikTokLiveApi apiInstance = new TikTokLiveApi(defaultClient);
 *   Object result = apiInstance.fetchWebcastURL(client, roomId, ...);
 *
 * Target pattern:
 *   EulerStreamApiClient client = EulerStreamApiClient.builder()
 *       .apiKey("YOUR_API_KEY")
 *       .build();
 *   Object result = client.webcast().fetchWebcastURL(roomId, ...);
 */

function resolvePropertyName(apiClassName: string, overrides: Record<string, string>): string {
  if (overrides[apiClassName]) return overrides[apiClassName];
  const stripped = apiClassName.replace(/Api$/, '');
  return stripped.charAt(0).toLowerCase() + stripped.slice(1);
}

function buildArgs(params: ParsedOperation['parameters']): string {
  if (params.length === 0) return '';
  return params.map(p => {
    if (p.defaultValue && p.defaultValue !== 'undefined') return `"${p.defaultValue}"`;
    switch (p.type.toLowerCase()) {
      case 'string': return `"${p.name}_value"`;
      case 'double':
      case 'number': return '0D';
      case 'boolean': return 'true';
      default: return `${p.name}`;
    }
  }).join(', ');
}

export const transformer: SdkTransformer = {
  transform(op: ParsedOperation, overrides: Record<string, string>): string {
    const prop = resolvePropertyName(op.apiClassName, overrides);
    const args = buildArgs(op.parameters);

    // Extract return type from signature: "> ReturnType methodName(...)"
    const retMatch = op.signature.match(/^(\S+)\s+\w+/);
    const returnType = retMatch ? retMatch[1] : 'Object';
    const hasReturn = returnType !== 'void';

    const call = `client.${prop}().${op.methodName}(${args})`;
    const lines = [
      `import io.github.isaackogan.EulerStreamApiClient;`,
      ``,
      `EulerStreamApiClient client = EulerStreamApiClient.builder()`,
      `    .apiKey("YOUR_API_KEY")`,
      `    .build();`,
      ``,
      hasReturn
        ? `${returnType} result = ${call};`
        : `${call};`,
    ];

    return lines.join('\n');
  },
};
