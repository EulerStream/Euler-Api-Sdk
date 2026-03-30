package com.eulerstream;

import com.eulerstream.api.AccountsApi;
import com.eulerstream.api.AnalyticsApi;
import com.eulerstream.api.AuthenticationApi;
import com.eulerstream.api.TikTokCaptchasApi;
import com.eulerstream.api.TikTokGeneralApi;
import com.eulerstream.api.TikTokLiveAlertTargetsApi;
import com.eulerstream.api.TikTokLiveAlertsApi;
import com.eulerstream.api.TikTokLiveApi;
import com.eulerstream.api.TikTokLiveModerationApi;
import com.eulerstream.api.TikTokLivePremiumApi;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

/**
 * Tests for {@link EulerStreamApiClient}.
 * Verifies builder pattern, default configuration, and that all API accessors return non-null instances.
 */
public class EulerStreamApiClientTest {

    @Test
    public void testBuildWithDefaults() {
        EulerStreamApiClient client = EulerStreamApiClient.builder().build();

        assertNotNull(client, "Client should not be null");
        assertNotNull(client.getApiClient(), "Underlying ApiClient should not be null");
        assertEquals(
                "https://tiktok.eulerstream.com",
                client.getApiClient().getBasePath(),
                "Default base path should be the EulerStream production URL"
        );
    }

    @Test
    public void testCreateDefault() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();

        assertNotNull(client, "Client from createDefault() should not be null");
        assertEquals(
                "https://tiktok.eulerstream.com",
                client.getApiClient().getBasePath(),
                "Default base path should be the EulerStream production URL"
        );
    }

    @Test
    public void testBuildWithCustomBasePath() {
        String customBasePath = "https://custom.example.com";
        EulerStreamApiClient client = EulerStreamApiClient.builder()
                .basePath(customBasePath)
                .build();

        assertEquals(
                customBasePath,
                client.getApiClient().getBasePath(),
                "Base path should match the custom value provided to the builder"
        );
    }

    @Test
    public void testBuildWithApiKey() {
        EulerStreamApiClient client = EulerStreamApiClient.builder()
                .apiKey("test-api-key-123")
                .build();

        assertNotNull(client, "Client built with an API key should not be null");
        assertNotNull(client.getApiClient(), "Underlying ApiClient should not be null");
    }

    @Test
    public void testBuildWithCustomBasePathAndApiKey() {
        String customBasePath = "https://staging.eulerstream.com";
        EulerStreamApiClient client = EulerStreamApiClient.builder()
                .basePath(customBasePath)
                .apiKey("my-key")
                .build();

        assertEquals(
                customBasePath,
                client.getApiClient().getBasePath(),
                "Base path should match the custom value"
        );
    }

    @Test
    public void testBuildWithCustomApiClient() {
        ApiClient customApiClient = new ApiClient();
        customApiClient.setBasePath("https://injected.example.com");

        EulerStreamApiClient client = EulerStreamApiClient.builder()
                .apiClient(customApiClient)
                .build();

        assertEquals(
                "https://injected.example.com",
                client.getApiClient().getBasePath(),
                "Should use the injected ApiClient's base path"
        );
    }

    @Test
    public void testAccountsApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        AccountsApi api = client.accounts();
        assertNotNull(api, "accounts() should return a non-null AccountsApi instance");
    }

    @Test
    public void testAnalyticsApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        AnalyticsApi api = client.analytics();
        assertNotNull(api, "analytics() should return a non-null AnalyticsApi instance");
    }

    @Test
    public void testAuthenticationApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        AuthenticationApi api = client.authentication();
        assertNotNull(api, "authentication() should return a non-null AuthenticationApi instance");
    }

    @Test
    public void testCaptchasApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        TikTokCaptchasApi api = client.captchas();
        assertNotNull(api, "captchas() should return a non-null TikTokCaptchasApi instance");
    }

    @Test
    public void testGeneralApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        TikTokGeneralApi api = client.general();
        assertNotNull(api, "general() should return a non-null TikTokGeneralApi instance");
    }

    @Test
    public void testAlertTargetsApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        TikTokLiveAlertTargetsApi api = client.alertTargets();
        assertNotNull(api, "alertTargets() should return a non-null TikTokLiveAlertTargetsApi instance");
    }

    @Test
    public void testAlertsApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        TikTokLiveAlertsApi api = client.alerts();
        assertNotNull(api, "alerts() should return a non-null TikTokLiveAlertsApi instance");
    }

    @Test
    public void testWebcastApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        TikTokLiveApi api = client.webcast();
        assertNotNull(api, "webcast() should return a non-null TikTokLiveApi instance");
    }

    @Test
    public void testModerationApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        TikTokLiveModerationApi api = client.moderation();
        assertNotNull(api, "moderation() should return a non-null TikTokLiveModerationApi instance");
    }

    @Test
    public void testPremiumApiNotNull() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        TikTokLivePremiumApi api = client.premium();
        assertNotNull(api, "premium() should return a non-null TikTokLivePremiumApi instance");
    }

    @Test
    public void testAllApiAccessorsReturnNonNull() {
        EulerStreamApiClient client = EulerStreamApiClient.builder()
                .apiKey("test-key")
                .build();

        assertNotNull(client.accounts(), "accounts() must not be null");
        assertNotNull(client.analytics(), "analytics() must not be null");
        assertNotNull(client.authentication(), "authentication() must not be null");
        assertNotNull(client.captchas(), "captchas() must not be null");
        assertNotNull(client.general(), "general() must not be null");
        assertNotNull(client.alertTargets(), "alertTargets() must not be null");
        assertNotNull(client.alerts(), "alerts() must not be null");
        assertNotNull(client.webcast(), "webcast() must not be null");
        assertNotNull(client.moderation(), "moderation() must not be null");
        assertNotNull(client.premium(), "premium() must not be null");
    }
}
