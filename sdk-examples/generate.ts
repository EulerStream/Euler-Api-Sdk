import { generate, loadConfig } from '@eulerstream/openapi-generator-examples';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SPEC_PATH = path.resolve(__dirname, '..', 'build', 'openapi.json');
const OUTPUT_DIR = path.resolve(__dirname, 'output');
const CONFIGS_DIR = path.resolve(__dirname, 'configs');

const languages = [
    { generator: 'typescript-axios', config: 'typescript.config.yml' },
    { generator: 'openapi-python-client', config: 'python.config.yml' },
    { generator: 'java', config: 'java.config.yml' },
    { generator: 'csharp', config: 'csharp.config.yml' },
    { generator: 'go', config: 'go.config.yml' },
    { generator: 'curl', config: 'curl.config.yml' },
];

for (const { generator, config: configFile } of languages) {
    const config = loadConfig(path.resolve(CONFIGS_DIR, configFile));

    // Resolve template path relative to this script's directory
    if (config.templatePath) {
        config.templatePath = path.resolve(__dirname, config.templatePath);
    }

    const result = generate({
        inputSpec: SPEC_PATH,
        generator,
        outputDir: OUTPUT_DIR,
        config,
    });

    console.log(`${result.languageId}: ${result.operationCount} operations, ${result.filesWritten.length} files written`);
}

console.log(`\nOutput written to: ${OUTPUT_DIR}`);
