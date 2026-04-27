package eulerstream_test

import (
	"net/http"
	"testing"

	eulerstream "github.com/EulerStream/Euler-Api-Sdk/sdk/go"
)

func TestNewEulerStreamClient_NoOptions(t *testing.T) {
	client := eulerstream.NewEulerStreamClient()
	if client == nil {
		t.Fatal("expected non-nil client, got nil")
	}
}

func TestNewEulerStreamClient_WithAPIKey(t *testing.T) {
	client := eulerstream.NewEulerStreamClient(eulerstream.WithAPIKey("test-key"))
	if client == nil {
		t.Fatal("expected non-nil client, got nil")
	}
}

func TestNewEulerStreamClient_WithHTTPClient(t *testing.T) {
	custom := &http.Client{}
	client := eulerstream.NewEulerStreamClient(eulerstream.WithHTTPClient(custom))
	if client == nil {
		t.Fatal("expected non-nil client, got nil")
	}
}

func TestNewEulerStreamClient_WithMultipleOptions(t *testing.T) {
	client := eulerstream.NewEulerStreamClient(
		eulerstream.WithAPIKey("test-key"),
		eulerstream.WithHTTPClient(&http.Client{}),
		eulerstream.WithServerIndex(0),
	)
	if client == nil {
		t.Fatal("expected non-nil client, got nil")
	}
}

func TestNewEulerStreamClient_RawClientAccessible(t *testing.T) {
	client := eulerstream.NewEulerStreamClient()
	if client.Raw == nil {
		t.Fatal("expected Raw (*eulerapi.APIClient) to be non-nil")
	}
}

func TestNewEulerStreamClient_AllServiceFieldsNonNil(t *testing.T) {
	client := eulerstream.NewEulerStreamClient()

	tests := []struct {
		name  string
		field interface{}
	}{
		{"Accounts", client.Accounts},
		{"Analytics", client.Analytics},
		{"Authentication", client.Authentication},
		{"Captchas", client.Captchas},
		{"General", client.General},
		{"Webcast", client.Webcast},
		{"AlertTargets", client.AlertTargets},
		{"Alerts", client.Alerts},
		{"Moderation", client.Moderation},
		{"Premium", client.Premium},
	}

	for _, tc := range tests {
		if tc.field == nil {
			t.Errorf("expected %s service field to be non-nil", tc.name)
		}
	}
}
