import { ParsedOperation, SdkTransformer } from './types';

/**
 * Transform raw openapi-generator TypeScript examples into EulerStreamApiClient wrapper examples.
 *
 * Raw pattern:
 *   import { XApi, Configuration } from './api';
 *   const configuration = new Configuration();
 *   const apiInstance = new XApi(configuration);
 *   const { status, data } = await apiInstance.method(arg1, arg2);
 *
 * Target pattern:
 *   import EulerStreamApiClient from '@eulerstream/euler-api-sdk';
 *   const client = new EulerStreamApiClient({ apiKey: 'YOUR_API_KEY' });
 *   const { status, data } = await client.webcast.method(arg1, arg2);
 */

function resolvePropertyName(apiClassName: string, overrides: Record<string, string>): string {
  if (overrides[apiClassName]) return overrides[apiClassName];
  const stripped = apiClassName.replace(/Api$/, '');
  return stripped.charAt(0).toLowerCase() + stripped.slice(1);
}

function buildArgs(params: ParsedOperation['parameters']): string {
  if (params.length === 0) return '';
  return params.map(p => {
    if (p.defaultValue && p.defaultValue !== 'undefined') return JSON.stringify(p.defaultValue);
    switch (p.type.toLowerCase()) {
      case 'string': return `"${p.name}_value"`;
      case 'number':
      case 'double': return '0';
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
    const hasReturn = retMatch && retMatch[1] !== 'void';

    const call = `client.${prop}.${op.methodName}(${args})`;
    const lines = [
      `import EulerStreamApiClient from '@eulerstream/euler-api-sdk';`,
      ``,
      `const client = new EulerStreamApiClient({ apiKey: 'YOUR_API_KEY' });`,
      hasReturn
        ? `const { status, data } = await ${call};`
        : `await ${call};`,
    ];

    return lines.join('\n');
  },
};
