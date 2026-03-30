import { AccountsApi,
  AnalyticsApi,
  AuthenticationApi,
  TikTokCaptchasApi,
  TikTokGeneralApi,
  TikTokLIVEApi,
  TikTokLIVEAlertTargetsApi,
  TikTokLIVEAlertsApi,
  TikTokLIVEModerationApi,
  TikTokLIVEPremiumApi } from "@/sdk";
import {buildConfig, ClientConfiguration} from "@/utils";

// Exports
export * from './sdk';
export * from './utils';

// Export an API Client
export default class EulerStreamApiClient {

  public readonly accounts: AccountsApi;
  public readonly analytics: AnalyticsApi;
  public readonly authentication: AuthenticationApi;
  public readonly captchas: TikTokCaptchasApi;
  public readonly general: TikTokGeneralApi;
  public readonly webcast: TikTokLIVEApi;
  public readonly alertTargets: TikTokLIVEAlertTargetsApi;
  public readonly alerts: TikTokLIVEAlertsApi;
  public readonly moderation: TikTokLIVEModerationApi;
  public readonly premium: TikTokLIVEPremiumApi;
  public readonly configuration: ClientConfiguration;

  /**
   * EulerStream API Client
   *
   * @param config The configuration for the API client
   */
  constructor(
      config: Partial<ClientConfiguration> = {}
  ) {

    // Build the config
    this.configuration = buildConfig(config);

    // Set up the APIs
    this.accounts = new AccountsApi(this.configuration);
    this.analytics = new AnalyticsApi(this.configuration);
    this.authentication = new AuthenticationApi(this.configuration);
    this.captchas = new TikTokCaptchasApi(this.configuration);
    this.general = new TikTokGeneralApi(this.configuration);
    this.webcast = new TikTokLIVEApi(this.configuration);
    this.alertTargets = new TikTokLIVEAlertTargetsApi(this.configuration);
    this.alerts = new TikTokLIVEAlertsApi(this.configuration);
    this.moderation = new TikTokLIVEModerationApi(this.configuration);
    this.premium = new TikTokLIVEPremiumApi(this.configuration);

  }

}
