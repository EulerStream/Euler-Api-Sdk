using System;
using Xunit;
using EulerApiSdk;
using EulerApiSdk.Api;

namespace EulerApiSdk.Tests
{
    public class BasicTests : IDisposable
    {
        private readonly EulerStreamApiClient _client;

        public BasicTests()
        {
            _client = new EulerStreamApiClient();
        }

        public void Dispose()
        {
            _client.Dispose();
        }

        [Fact]
        public void Client_CanBeInstantiated()
        {
            // The client was already created in the constructor; just verify it is not null.
            Assert.NotNull(_client);
        }

        [Fact]
        public void Client_ImplementsIDisposable()
        {
            Assert.IsAssignableFrom<IDisposable>(_client);
        }

        [Fact]
        public void Accounts_IsNotNull()
        {
            Assert.NotNull(_client.Accounts);
        }

        [Fact]
        public void Analytics_IsNotNull()
        {
            Assert.NotNull(_client.Analytics);
        }

        [Fact]
        public void Authentication_IsNotNull()
        {
            Assert.NotNull(_client.Authentication);
        }

        [Fact]
        public void Captchas_IsNotNull()
        {
            Assert.NotNull(_client.Captchas);
        }

        [Fact]
        public void General_IsNotNull()
        {
            Assert.NotNull(_client.General);
        }

        [Fact]
        public void Webcast_IsNotNull()
        {
            Assert.NotNull(_client.Webcast);
        }

        [Fact]
        public void AlertTargets_IsNotNull()
        {
            Assert.NotNull(_client.AlertTargets);
        }

        [Fact]
        public void Alerts_IsNotNull()
        {
            Assert.NotNull(_client.Alerts);
        }

        [Fact]
        public void Moderation_IsNotNull()
        {
            Assert.NotNull(_client.Moderation);
        }

        [Fact]
        public void Premium_IsNotNull()
        {
            Assert.NotNull(_client.Premium);
        }

        [Fact]
        public void AllApiProperties_ImplementCorrectInterfaces()
        {
            Assert.IsAssignableFrom<IAccountsApi>(_client.Accounts);
            Assert.IsAssignableFrom<IAnalyticsApi>(_client.Analytics);
            Assert.IsAssignableFrom<IAuthenticationApi>(_client.Authentication);
            Assert.IsAssignableFrom<ITikTokCaptchasApi>(_client.Captchas);
            Assert.IsAssignableFrom<ITikTokGeneralApi>(_client.General);
            Assert.IsAssignableFrom<ITikTokLIVEApi>(_client.Webcast);
            Assert.IsAssignableFrom<ITikTokLIVEAlertTargetsApi>(_client.AlertTargets);
            Assert.IsAssignableFrom<ITikTokLIVEAlertsApi>(_client.Alerts);
            Assert.IsAssignableFrom<ITikTokLIVEModerationApi>(_client.Moderation);
            Assert.IsAssignableFrom<ITikTokLIVEPremiumApi>(_client.Premium);
        }

        [Fact]
        public void Client_CanBeCreatedWithCustomBaseAddress()
        {
            using var customClient = new EulerStreamApiClient(baseAddress: "https://custom.example.com");
            Assert.NotNull(customClient);
        }

        [Fact]
        public void Client_CanBeDisposedMultipleTimes()
        {
            var client = new EulerStreamApiClient();
            client.Dispose();
            // Second dispose should not throw
            client.Dispose();
        }
    }
}
