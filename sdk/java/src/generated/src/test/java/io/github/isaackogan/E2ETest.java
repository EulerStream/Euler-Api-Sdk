package io.github.isaackogan;

import io.github.isaackogan.model.HostsResponse;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class E2ETest {

    @Test
    public void testGetHostsReturnsData() throws Exception {
        EulerStreamApiClient client = EulerStreamApiClient.createDefault();
        HostsResponse response = client.analytics().getHosts();
        assertNotNull(response);
        assertNotNull(response.getHosts());
        assertFalse(response.getHosts().isEmpty());
    }
}
