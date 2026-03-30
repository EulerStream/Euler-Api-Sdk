package com.eulerstream;

import com.eulerstream.model.HostsResponse;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;

/**
 * End-to-end test that makes a real HTTP call through the SDK.
 */
public class E2ETest {

    @Test
    public void testGetHostsReturnsValidResponse() throws ApiException {
        EulerStreamApiClient client = EulerStreamApiClient.builder().build();

        HostsResponse response = client.analytics().getHosts();

        assertNotNull(response, "Response should not be null");
        assertNotNull(response.getHosts(), "Hosts list should not be null");
        assertFalse(response.getHosts().isEmpty(), "Hosts list should not be empty");
    }
}
