export interface ParsedOperation {
  /** Method name as it appears in the SDK docs (e.g. fetchWebcastURL, FetchAgents) */
  methodName: string;
  /** The signature line from the docs (e.g. "> Object fetchWebcastURL(...)") */
  signature: string;
  /** Raw code example extracted from the markdown code block */
  rawExample: string;
  /** The API class name from the doc filename (e.g. TikTokLIVEApi, AnalyticsAPI) */
  apiClassName: string;
  /** Parameters parsed from the markdown table */
  parameters: ParamInfo[];
}

export interface ParamInfo {
  name: string;
  type: string;
  description: string;
  optional: boolean;
  defaultValue?: string;
}

export interface SpecOperation {
  operationId: string;
  tag: string;
  method: string;
  path: string;
  parameters: any[];
  hasBody: boolean;
  description?: string;
}

export interface SdkTransformer {
  /**
   * Transform a parsed operation into a clean wrapper-client example.
   * @param op The parsed operation from markdown docs
   * @param overrides The API class name -> property name mapping
   * @returns The transformed code example string
   */
  transform(op: ParsedOperation, overrides: Record<string, string>): string;
}
