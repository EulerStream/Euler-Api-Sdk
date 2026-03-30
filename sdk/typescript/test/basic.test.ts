import assert from "node:assert";
import EulerStreamApiClient, { buildConfig } from "../src/index.js";
import {
    AccountsApi,
    AnalyticsApi,
    AuthenticationApi,
    TikTokCaptchasApi,
    TikTokGeneralApi,
    TikTokLIVEApi,
    TikTokLIVEAlertTargetsApi,
    TikTokLIVEAlertsApi,
    TikTokLIVEModerationApi,
    TikTokLIVEPremiumApi,
} from "../src/sdk/index.js";

let passed = 0;
let failed = 0;

function test(name: string, fn: () => void): void {
    try {
        fn();
        console.log(`  PASS: ${name}`);
        passed++;
    } catch (err: any) {
        console.error(`  FAIL: ${name}`);
        console.error(`        ${err.message}`);
        failed++;
    }
}

console.log("\n--- EulerStreamApiClient tests ---\n");

// 1. Can be instantiated with no arguments
test("EulerStreamApiClient can be instantiated with no arguments", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client, "client should be truthy");
});

// 2. All API properties exist and are correct instances
test("client.accounts is an AccountsApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.accounts instanceof AccountsApi);
});

test("client.analytics is an AnalyticsApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.analytics instanceof AnalyticsApi);
});

test("client.authentication is an AuthenticationApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.authentication instanceof AuthenticationApi);
});

test("client.captchas is a TikTokCaptchasApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.captchas instanceof TikTokCaptchasApi);
});

test("client.general is a TikTokGeneralApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.general instanceof TikTokGeneralApi);
});

test("client.webcast is a TikTokLIVEApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.webcast instanceof TikTokLIVEApi);
});

test("client.alertTargets is a TikTokLIVEAlertTargetsApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.alertTargets instanceof TikTokLIVEAlertTargetsApi);
});

test("client.alerts is a TikTokLIVEAlertsApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.alerts instanceof TikTokLIVEAlertsApi);
});

test("client.moderation is a TikTokLIVEModerationApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.moderation instanceof TikTokLIVEModerationApi);
});

test("client.premium is a TikTokLIVEPremiumApi instance", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.premium instanceof TikTokLIVEPremiumApi);
});

// 3. Client exposes the configuration property
test("client exposes configuration property", () => {
    const client = new EulerStreamApiClient();
    assert.ok(client.configuration !== undefined, "configuration should be defined");
    assert.ok(typeof client.configuration === "object", "configuration should be an object");
});

// 4. buildConfig returns correct defaults
console.log("\n--- buildConfig tests ---\n");

test("buildConfig returns default basePath", () => {
    const config = buildConfig({});
    assert.strictEqual(config.basePath, "https://tiktok.eulerstream.com");
});

test("buildConfig returns baseOptions with validateStatus", () => {
    const config = buildConfig({});
    assert.ok(config.baseOptions, "baseOptions should be defined");
    assert.ok(typeof config.baseOptions.validateStatus === "function", "validateStatus should be a function");
    assert.strictEqual(config.baseOptions.validateStatus(404), true, "validateStatus should always return true");
    assert.strictEqual(config.baseOptions.validateStatus(500), true, "validateStatus should always return true");
});

test("buildConfig returns isJsonMime function", () => {
    const config = buildConfig({});
    assert.ok(typeof config.isJsonMime === "function", "isJsonMime should be a function");
    assert.strictEqual(config.isJsonMime("application/json"), true);
    assert.strictEqual(config.isJsonMime("text/html"), false);
});

test("buildConfig allows overriding basePath", () => {
    const config = buildConfig({ basePath: "https://custom.example.com" });
    assert.strictEqual(config.basePath, "https://custom.example.com");
});

// 5. Configuration with a custom apiKey
test("buildConfig sets X-Api-Key header when apiKey is provided", () => {
    const config = buildConfig({ apiKey: "my-test-key-123" });
    assert.ok(config.baseOptions, "baseOptions should be defined");
    assert.ok(config.baseOptions.headers, "headers should be defined");
    assert.strictEqual(config.baseOptions.headers["X-Api-Key"], "my-test-key-123");
});

test("buildConfig removes apiKey from config after setting header", () => {
    const config = buildConfig({ apiKey: "my-test-key-123" });
    assert.strictEqual(config.apiKey, undefined, "apiKey should be removed from config");
});

test("buildConfig does not set X-Api-Key header when apiKey is absent", () => {
    const config = buildConfig({});
    assert.ok(config.baseOptions, "baseOptions should be defined");
    const xApiKey = config.baseOptions.headers?.["X-Api-Key"];
    assert.strictEqual(xApiKey, undefined, "X-Api-Key header should not be set");
});

// 6. Client constructed with apiKey passes it through to configuration
test("EulerStreamApiClient passes apiKey through to configuration headers", () => {
    const client = new EulerStreamApiClient({ apiKey: "sdk-key-456" });
    assert.strictEqual(
        client.configuration.baseOptions?.headers?.["X-Api-Key"],
        "sdk-key-456",
    );
});

// Summary
console.log(`\n--- Results: ${passed} passed, ${failed} failed ---\n`);

if (failed > 0) {
    process.exit(1);
}
