import { ParsedOperation, SdkTransformer } from './types';

/**
 * Transform raw openapi-generator Go examples into EulerStreamClient wrapper examples.
 *
 * Raw pattern:
 *   openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
 *   configuration := openapiclient.NewConfiguration()
 *   apiClient := openapiclient.NewAPIClient(configuration)
 *   resp, r, err := apiClient.AnalyticsAPI.FetchAgents(context.Background()).Execute()
 *
 * Target pattern:
 *   eulerstream "github.com/EulerStream/Euler-Api-Sdk/sdk/go"
 *   client := eulerstream.NewEulerStreamClient(eulerstream.WithAPIKey("YOUR_API_KEY"))
 *   resp, _, err := client.Analytics.FetchAgents(context.Background()).Execute()
 */

function resolvePropertyName(apiClassName: string, overrides: Record<string, string>): string {
  if (overrides[apiClassName]) return overrides[apiClassName];
  // Go uses PascalCase
  return apiClassName.replace(/API$/, '');
}

function buildChainedArgs(params: ParsedOperation['parameters']): string {
  if (params.length === 0) return '';
  return params.map(p => {
    const pascalName = p.name.charAt(0).toUpperCase() + p.name.slice(1);
    switch (p.type.toLowerCase()) {
      case 'string': return `.${pascalName}("${p.name}_value")`;
      case 'float64':
      case 'number':
      case 'double': return `.${pascalName}(0)`;
      case 'bool':
      case 'boolean': return `.${pascalName}(true)`;
      default: return `.${pascalName}(${p.name})`;
    }
  }).join('');
}

export const transformer: SdkTransformer = {
  transform(op: ParsedOperation, overrides: Record<string, string>): string {
    const prop = resolvePropertyName(op.apiClassName, overrides);
    const chain = buildChainedArgs(op.parameters);

    const lines = [
      `import (`,
      `\t"context"`,
      `\teulerstream "github.com/EulerStream/Euler-Api-Sdk/sdk/go"`,
      `)`,
      ``,
      `client := eulerstream.NewEulerStreamClient(`,
      `\teulerstream.WithAPIKey("YOUR_API_KEY"),`,
      `)`,
      ``,
      `resp, _, err := client.${prop}.${op.methodName}(context.Background())${chain}.Execute()`,
    ];

    return lines.join('\n');
  },
};
