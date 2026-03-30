package io.github.isaackogan;

import io.github.isaackogan.api.*;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class EulerStreamApiClientTest {

    @Test
    public void testBuildWithDefaults() {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        assertNotNull(client);
    }

    @Test
    public void testBuildWithApiKey() {
        EulerStreamApiClient client = EulerStreamApiClient.builder()
                .apiKey("test-key")
                .build();
        assertNotNull(client);
    }

    @Test
    public void testAllApiAccessorsReturnNonNull() {
        EulerStreamApiClient client = EulerStreamApiClient.builder()
                .apiKey("test-key")
                .build();
        assertNotNull(client.accounts());
        assertNotNull(client.analytics());
        assertNotNull(client.authentication());
        assertNotNull(client.captchas());
        assertNotNull(client.general());
        assertNotNull(client.webcast());
        assertNotNull(client.alertTargets());
        assertNotNull(client.alerts());
        assertNotNull(client.moderation());
        assertNotNull(client.premium());
    }
}
