import * as fs from 'fs';
import * as path from 'path';
import * as assert from 'assert';
import { execSync } from 'child_process';

const TEST_DIR: string = path.resolve(__dirname, '.test-fixtures');
const SCRIPT: string = path.resolve(__dirname, 'fix-enum-conflicts.ts');

function setup(): void {
    fs.mkdirSync(TEST_DIR, { recursive: true });
}

function teardown(): void {
    fs.rmSync(TEST_DIR, { recursive: true, force: true });
}

function writeModel(filename: string, content: string): void {
    fs.writeFileSync(path.join(TEST_DIR, filename), content, 'utf-8');
}

function readModel(filename: string): string {
    return fs.readFileSync(path.join(TEST_DIR, filename), 'utf-8');
}

function runFix(): string {
    return execSync(`npx tsx ${SCRIPT} ${TEST_DIR}`, { encoding: 'utf-8' });
}

// ── Tests ──────────────────────────────────────────────────────

let passed = 0;
let failed = 0;

function test(name: string, fn: () => void): void {
    try {
        setup();
        fn();
        console.log(`  ✓ ${name}`);
        passed++;
    } catch (e: any) {
        console.error(`  ✗ ${name}`);
        console.error(`    ${e.message}`);
        failed++;
    } finally {
        teardown();
    }
}

console.log('fix-enum-conflicts tests:\n');

test('prefixes numeric constants with type name', () => {
    writeModel('model_account_scopes.go', `package eulerapi

type AccountScopes float32

const (
\t_0 AccountScopes = 0
\t_1 AccountScopes = 1
)
`);
    runFix();
    const result: string = readModel('model_account_scopes.go');
    assert.ok(result.includes('ACCOUNT_SCOPES_0 AccountScopes = 0'), 'Expected ACCOUNT_SCOPES_0');
    assert.ok(result.includes('ACCOUNT_SCOPES_1 AccountScopes = 1'), 'Expected ACCOUNT_SCOPES_1');
    assert.ok(!result.includes('\t_0 '), 'Old _0 should be gone');
    assert.ok(!result.includes('\t_1 '), 'Old _1 should be gone');
});

test('prefixes string constants with type name', () => {
    writeModel('model_proxy_region.go', `package eulerapi

type ProxyRegion string

const (
\tDE ProxyRegion = "DE"
\tFR ProxyRegion = "FR"
)
`);
    runFix();
    const result: string = readModel('model_proxy_region.go');
    assert.ok(result.includes('PROXY_REGION_DE ProxyRegion = "DE"'), 'Expected PROXY_REGION_DE');
    assert.ok(result.includes('PROXY_REGION_FR ProxyRegion = "FR"'), 'Expected PROXY_REGION_FR');
});

test('resolves conflicts between two files with same constant names', () => {
    writeModel('model_type_a.go', `package eulerapi

type TypeA float32

const (
\t_0 TypeA = 0
\t_1 TypeA = 1
)
`);
    writeModel('model_type_b.go', `package eulerapi

type TypeB float32

const (
\t_0 TypeB = 0
\t_1 TypeB = 1
)
`);
    runFix();
    const a: string = readModel('model_type_a.go');
    const b: string = readModel('model_type_b.go');
    assert.ok(a.includes('TYPE_A_0 TypeA = 0'), 'Expected TYPE_A_0');
    assert.ok(b.includes('TYPE_B_0 TypeB = 0'), 'Expected TYPE_B_0');
    assert.ok(a.includes('TYPE_A_1 TypeA = 1'), 'Expected TYPE_A_1');
    assert.ok(b.includes('TYPE_B_1 TypeB = 1'), 'Expected TYPE_B_1');
});

test('handles MINUS prefix in negative constants', () => {
    writeModel('model_duration.go', `package eulerapi

type Duration float32

const (
\t_MINUS_1 Duration = -1
\t_0 Duration = 0
)
`);
    runFix();
    const result: string = readModel('model_duration.go');
    assert.ok(result.includes('DURATION_MINUS_1 Duration = -1'), 'Expected DURATION_MINUS_1');
    assert.ok(result.includes('DURATION_0 Duration = 0'), 'Expected DURATION_0');
});

test('handles PascalCase type names correctly', () => {
    writeModel('model_tik_tok_live.go', `package eulerapi

type TikTokLIVEStatus float32

const (
\t_0 TikTokLIVEStatus = 0
)
`);
    runFix();
    const result: string = readModel('model_tik_tok_live.go');
    assert.ok(result.includes('TIK_TOK_LIVE_STATUS_0 TikTokLIVEStatus = 0'), 'Expected TIK_TOK_LIVE_STATUS_0');
});

test('does not modify non-model files', () => {
    writeModel('client.go', `package eulerapi

const (
\tDE Region = "DE"
)
`);
    runFix();
    const result: string = readModel('client.go');
    assert.ok(result.includes('\tDE Region = "DE"'), 'Non-model file should be untouched');
});

test('removes generated test directory', () => {
    const testDir: string = path.join(TEST_DIR, 'test');
    fs.mkdirSync(testDir, { recursive: true });
    fs.writeFileSync(path.join(testDir, 'api_test.go'), 'package test', 'utf-8');
    writeModel('model_dummy.go', `package eulerapi
`);
    runFix();
    assert.ok(!fs.existsSync(testDir), 'test directory should be removed');
});

test('reports correct count', () => {
    writeModel('model_a.go', `package eulerapi

type A float32

const (
\t_0 A = 0
\t_1 A = 1
\t_2 A = 2
)
`);
    const output: string = runFix();
    assert.ok(output.includes('Fixed 3 enum constants'), `Expected "Fixed 3", got: ${output.trim()}`);
});

// ── Summary ────────────────────────────────────────────────────

console.log(`\n${passed} passed, ${failed} failed`);
if (failed > 0) process.exit(1);
