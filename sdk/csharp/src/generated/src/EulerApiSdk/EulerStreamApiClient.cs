#nullable enable

using System;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using EulerApiSdk.Api;
using EulerApiSdk.Client;
using EulerApiSdk.Extensions;

namespace EulerApiSdk
{
    /// <summary>
    /// EulerStream API Client — a convenient wrapper that exposes all generated
    /// API groups as properties and manages the underlying DI container.
    /// </summary>
    public sealed class EulerStreamApiClient : IDisposable
    {
        private readonly ServiceProvider _serviceProvider;

        /// <summary>
        /// Accounts API group.
        /// </summary>
        public IAccountsApi Accounts { get; }

        /// <summary>
        /// Analytics API group.
        /// </summary>
        public IAnalyticsApi Analytics { get; }

        /// <summary>
        /// Authentication API group.
        /// </summary>
        public IAuthenticationApi Authentication { get; }

        /// <summary>
        /// Captchas API group.
        /// </summary>
        public ITikTokCaptchasApi Captchas { get; }

        /// <summary>
        /// General API group.
        /// </summary>
        public ITikTokGeneralApi General { get; }

        /// <summary>
        /// AlertTargets API group.
        /// </summary>
        public ITikTokLIVEAlertTargetsApi AlertTargets { get; }

        /// <summary>
        /// Alerts API group.
        /// </summary>
        public ITikTokLIVEAlertsApi Alerts { get; }

        /// <summary>
        /// Webcast API group.
        /// </summary>
        public ITikTokLIVEApi Webcast { get; }

        /// <summary>
        /// Moderation API group.
        /// </summary>
        public ITikTokLIVEModerationApi Moderation { get; }

        /// <summary>
        /// Premium API group.
        /// </summary>
        public ITikTokLIVEPremiumApi Premium { get; }

        /// <summary>
        /// Creates a new EulerStream API Client.
        /// </summary>
        /// <param name="configure">
        /// Optional callback to customise the <see cref="HostConfiguration"/>
        /// (e.g. add tokens, override HttpClient settings).
        /// </param>
        /// <param name="baseAddress">
        /// Override the default base address for API requests.
        /// </param>
        public EulerStreamApiClient(
            Action<HostConfiguration>? configure = null,
            string? baseAddress = null)
        {
            var services = new ServiceCollection();

            // Add logging (required by the generated API classes)
            services.AddLogging(builder => builder.AddConsole().SetMinimumLevel(LogLevel.Warning));

            // Register the generated SDK services
            services.AddApi(host =>
            {
                host.AddApiHttpClients(client =>
                {
                    client.BaseAddress = new Uri(baseAddress ?? ClientUtils.BASE_ADDRESS);
                });

                // Register a default placeholder API key token so the DI container
                // can always resolve TokenProvider<ApiKeyToken>.  When the caller
                // supplies real tokens via the configure callback, the later
                // registration wins (Microsoft DI last-wins semantics).
                host.AddTokens(new ApiKeyToken("", ClientUtils.ApiKeyHeader.ApiKey, prefix: ""));

                // Allow the caller to further configure (e.g. add tokens)
                configure?.Invoke(host);
            });

            _serviceProvider = services.BuildServiceProvider();

            // Resolve API instances
            Accounts = _serviceProvider.GetRequiredService<IAccountsApi>();
            Analytics = _serviceProvider.GetRequiredService<IAnalyticsApi>();
            Authentication = _serviceProvider.GetRequiredService<IAuthenticationApi>();
            Captchas = _serviceProvider.GetRequiredService<ITikTokCaptchasApi>();
            General = _serviceProvider.GetRequiredService<ITikTokGeneralApi>();
            AlertTargets = _serviceProvider.GetRequiredService<ITikTokLIVEAlertTargetsApi>();
            Alerts = _serviceProvider.GetRequiredService<ITikTokLIVEAlertsApi>();
            Webcast = _serviceProvider.GetRequiredService<ITikTokLIVEApi>();
            Moderation = _serviceProvider.GetRequiredService<ITikTokLIVEModerationApi>();
            Premium = _serviceProvider.GetRequiredService<ITikTokLIVEPremiumApi>();
        }

        /// <inheritdoc />
        public void Dispose()
        {
            _serviceProvider.Dispose();
        }
    }
}
