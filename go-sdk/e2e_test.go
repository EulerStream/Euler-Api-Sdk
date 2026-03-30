package eulerstream

import (
	"context"
	"net/http"
	"testing"
)

func TestGetHosts_E2E(t *testing.T) {
	client := NewEulerStreamClient()

	hosts, httpResp, err := client.Analytics.GetHosts(context.Background()).Execute()
	if err != nil {
		t.Fatalf("GetHosts returned error: %v", err)
	}

	if httpResp.StatusCode != http.StatusOK {
		t.Fatalf("expected status 200, got %d", httpResp.StatusCode)
	}

	if hosts == nil {
		t.Fatal("expected non-nil HostsResponse, got nil")
	}

	if hosts.GetCode() != 0 {
		t.Fatalf("expected response code 0, got %v", hosts.GetCode())
	}
}
