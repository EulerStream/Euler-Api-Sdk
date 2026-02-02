"""Contains all the data models used in inputs/outputs"""

from .account import Account
from .account_config import AccountConfig
from .account_scopes import AccountScopes
from .account_with_permissions_safe import AccountWithPermissionsSafe
from .accounts_table_request_limits import AccountsTableRequestLimits
from .alert import Alert
from .alert_config import AlertConfig
from .alert_target import AlertTarget
from .alert_target_config import AlertTargetConfig
from .alert_target_format import AlertTargetFormat
from .alert_target_status import AlertTargetStatus
from .api_key import ApiKey
from .api_key_config import ApiKeyConfig
from .captcha_credits_response import CaptchaCreditsResponse
from .complete_icon_captcha_body import CompleteIconCaptchaBody
from .complete_puzzle_captcha_body import CompletePuzzleCaptchaBody
from .complete_shapes_captcha_body import CompleteShapesCaptchaBody
from .complete_whirl_captcha_body import CompleteWhirlCaptchaBody
from .create_alert_body import CreateAlertBody
from .create_alert_response import CreateAlertResponse
from .create_alert_target_payload import CreateAlertTargetPayload
from .create_alert_target_response import CreateAlertTargetResponse
from .create_jwt_response import CreateJWTResponse
from .create_key_payload import CreateKeyPayload
from .create_key_response import CreateKeyResponse
from .delete_alert_response import DeleteAlertResponse
from .delete_alert_target_response import DeleteAlertTargetResponse
from .delete_key_delete_by import DeleteKeyDeleteBy
from .delete_key_response import DeleteKeyResponse
from .exchange_token_request import ExchangeTokenRequest
from .exchange_token_request_grant_type import ExchangeTokenRequestGrantType
from .get_key_retrieve_by import GetKeyRetrieveBy
from .get_rate_limits import GetRateLimits
from .get_sign_webcast_url_response import GetSignWebcastUrlResponse
from .hashtag_list_api_response import HashtagListAPIResponse
from .hosts_response import HostsResponse
from .icon_captcha_response import IconCaptchaResponse
from .icons_result import IconsResult
from .json_response import JSONResponse
from .jwt_config import JWTConfig
from .jwt_config_web_socket_data import JWTConfigWebSocketData
from .jwt_create_config import JWTCreateConfig
from .jwt_create_config_web_socket_data import JWTCreateConfigWebSocketData
from .list_alert_targets_response import ListAlertTargetsResponse
from .list_alerts_response import ListAlertsResponse
from .list_keys_response import ListKeysResponse
from .live_analytics_video_detail_api_response import LiveAnalyticsVideoDetailAPIResponse
from .live_analytics_video_list_api_response import LiveAnalyticsVideoListAPIResponse
from .load_shed_info import LoadShedInfo
from .mute_duration import MuteDuration
from .o_auth_revoke_response import OAuthRevokeResponse
from .o_auth_scope import OAuthScope
from .o_auth_token_response import OAuthTokenResponse
from .oxy_labs_proxy_region import OxyLabsProxyRegion
from .partial_signed_url_info import PartialSignedUrlInfo
from .partial_tiktok_live_user_info import PartialTikTokLiveUserInfo
from .partial_tiktok_user_info import PartialTikTokUserInfo
from .partial_webcast_region_rankings_output_rank import PartialWebcastRegionRankingsOutputRank
from .partial_webcast_region_rankings_output_rank_user import PartialWebcastRegionRankingsOutputRankUser
from .peer_presence import PeerPresence
from .peer_presence_type import PeerPresenceType
from .peer_role import PeerRole
from .point import Point
from .proxy_sign_result import ProxySignResult
from .puzzle_captcha_response import PuzzleCaptchaResponse
from .puzzle_result import PuzzleResult
from .rate_limit_info import RateLimitInfo
from .record_string_any import RecordStringAny
from .record_string_boolean_or_number import RecordStringBooleanOrNumber
from .record_string_is_live_boolean_room_id_string_or_null import RecordStringIsLiveBooleanRoomIdStringOrNull
from .record_string_is_live_boolean_room_id_string_or_null_additional_property import (
    RecordStringIsLiveBooleanRoomIdStringOrNullAdditionalProperty,
)
from .record_string_number import RecordStringNumber
from .record_string_string import RecordStringString
from .record_string_unknown import RecordStringUnknown
from .retrieve_account_response import RetrieveAccountResponse
from .retrieve_agent_hosts_response import RetrieveAgentHostsResponse
from .retrieve_alert_response import RetrieveAlertResponse
from .retrieve_alert_response_creator import RetrieveAlertResponseCreator
from .retrieve_bulk_live_check_payload import RetrieveBulkLiveCheckPayload
from .retrieve_bulk_live_check_payload_v1 import RetrieveBulkLiveCheckPayloadV1
from .retrieve_bulk_live_check_response import RetrieveBulkLiveCheckResponse
from .retrieve_key_response import RetrieveKeyResponse
from .retrieve_webcast_rankings_rank_type import RetrieveWebcastRankingsRankType
from .revoke_request_body import RevokeRequestBody
from .revoke_request_body_token_type_hint import RevokeRequestBodyTokenTypeHint
from .room_admin_update_api_response import RoomAdminUpdateAPIResponse
from .room_comments_toggle_api_response import RoomCommentsToggleAPIResponse
from .room_kick_user_api_response import RoomKickUserAPIResponse
from .room_kicked_users_api_response import RoomKickedUsersAPIResponse
from .room_moderators_api_response import RoomModeratorsAPIResponse
from .room_mute_user_api_response import RoomMuteUserAPIResponse
from .room_muted_users_api_response import RoomMutedUsersAPIResponse
from .room_unkick_user_api_response import RoomUnkickUserAPIResponse
from .room_unmute_user_api_response import RoomUnmuteUserAPIResponse
from .shapes_captcha_response import ShapesCaptchaResponse
from .shapes_result import ShapesResult
from .sign_tik_tok_url_body import SignTikTokUrlBody
from .sign_tik_tok_url_body_method import SignTikTokUrlBodyMethod
from .sign_tik_tok_url_body_type import SignTikTokUrlBodyType
from .sign_tik_tok_url_response import SignTikTokUrlResponse
from .soax_proxy_region import SoaxProxyRegion
from .solve_response_icons_result import SolveResponseIconsResult
from .solve_response_puzzle_result import SolveResponsePuzzleResult
from .solve_response_shapes_result import SolveResponseShapesResult
from .solve_response_whirl_result import SolveResponseWhirlResult
from .stream_type import StreamType
from .test_alert_target_response import TestAlertTargetResponse
from .tik_tok_live_user import TikTokLiveUser
from .tik_tok_live_user_raw import TikTokLiveUserRaw
from .tik_tok_live_user_user import TikTokLiveUserUser
from .token_error_response import TokenErrorResponse
from .token_response import TokenResponse
from .token_response_token_type import TokenResponseTokenType
from .uint_8_array import Uint8Array
from .update_key_payload import UpdateKeyPayload
from .update_key_response import UpdateKeyResponse
from .update_key_update_by import UpdateKeyUpdateBy
from .webcast_feed_response import WebcastFeedResponse
from .webcast_feed_response_extra import WebcastFeedResponseExtra
from .webcast_feed_response_extra_log_pb import WebcastFeedResponseExtraLogPb
from .webcast_feed_response_hashtag import WebcastFeedResponseHashtag
from .webcast_feed_response_hashtag_image import WebcastFeedResponseHashtagImage
from .webcast_feed_response_image import WebcastFeedResponseImage
from .webcast_feed_response_item import WebcastFeedResponseItem
from .webcast_feed_response_room_data import WebcastFeedResponseRoomData
from .webcast_feed_response_room_data_blurred_cover import WebcastFeedResponseRoomDataBlurredCover
from .webcast_feed_response_room_data_feed_room_label import WebcastFeedResponseRoomDataFeedRoomLabel
from .webcast_feed_response_room_data_game_tag_detail import WebcastFeedResponseRoomDataGameTagDetail
from .webcast_feed_response_room_data_rectangle_cover_img import WebcastFeedResponseRoomDataRectangleCoverImg
from .webcast_feed_response_room_data_square_cover_img import WebcastFeedResponseRoomDataSquareCoverImg
from .webcast_feed_response_room_data_stats import WebcastFeedResponseRoomDataStats
from .webcast_feed_response_room_data_taxonomy_tag_info import WebcastFeedResponseRoomDataTaxonomyTagInfo
from .webcast_feed_response_stream_url import WebcastFeedResponseStreamUrl
from .webcast_feed_response_stream_url_flv_pull_url import WebcastFeedResponseStreamUrlFlvPullUrl
from .webcast_feed_response_stream_url_live_core_sdk_data import WebcastFeedResponseStreamUrlLiveCoreSdkData
from .webcast_feed_response_stream_url_live_core_sdk_data_pull_data import (
    WebcastFeedResponseStreamUrlLiveCoreSdkDataPullData,
)
from .webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options import (
    WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptions,
)
from .webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options_default_quality import (
    WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptionsDefaultQuality,
)
from .webcast_feed_response_user import WebcastFeedResponseUser
from .webcast_feed_response_user_follow_info import WebcastFeedResponseUserFollowInfo
from .webcast_feed_response_user_own_room import WebcastFeedResponseUserOwnRoom
from .webcast_feed_route_output import WebcastFeedRouteOutput
from .webcast_feed_route_response import WebcastFeedRouteResponse
from .webcast_fetch_platform import WebcastFetchPlatform
from .webcast_gift_info_output import WebcastGiftInfoOutput
from .webcast_gift_info_route_response import WebcastGiftInfoRouteResponse
from .webcast_hashtag_list_response import WebcastHashtagListResponse
from .webcast_hashtag_list_response_data import WebcastHashtagListResponseData
from .webcast_hashtag_list_response_extra import WebcastHashtagListResponseExtra
from .webcast_hashtag_list_response_game_category import WebcastHashtagListResponseGameCategory
from .webcast_hashtag_list_response_game_tag import WebcastHashtagListResponseGameTag
from .webcast_hashtag_list_response_hashtag import WebcastHashtagListResponseHashtag
from .webcast_hashtag_list_response_hashtag_simple import WebcastHashtagListResponseHashtagSimple
from .webcast_hashtag_list_response_image import WebcastHashtagListResponseImage
from .webcast_hashtag_list_route_output import WebcastHashtagListRouteOutput
from .webcast_is_live_output import WebcastIsLiveOutput
from .webcast_live_analytics_video_detail_response import WebcastLiveAnalyticsVideoDetailResponse
from .webcast_live_analytics_video_detail_response_analytics import WebcastLiveAnalyticsVideoDetailResponseAnalytics
from .webcast_live_analytics_video_detail_response_average_watch_time import (
    WebcastLiveAnalyticsVideoDetailResponseAverageWatchTime,
)
from .webcast_live_analytics_video_detail_response_behavior_summary import (
    WebcastLiveAnalyticsVideoDetailResponseBehaviorSummary,
)
from .webcast_live_analytics_video_detail_response_cohost_summary import (
    WebcastLiveAnalyticsVideoDetailResponseCohostSummary,
)
from .webcast_live_analytics_video_detail_response_comments_info import (
    WebcastLiveAnalyticsVideoDetailResponseCommentsInfo,
)
from .webcast_live_analytics_video_detail_response_data import WebcastLiveAnalyticsVideoDetailResponseData
from .webcast_live_analytics_video_detail_response_detailed_metrics import (
    WebcastLiveAnalyticsVideoDetailResponseDetailedMetrics,
)
from .webcast_live_analytics_video_detail_response_diamonds_details import (
    WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails,
)
from .webcast_live_analytics_video_detail_response_earnings import WebcastLiveAnalyticsVideoDetailResponseEarnings
from .webcast_live_analytics_video_detail_response_extra import WebcastLiveAnalyticsVideoDetailResponseExtra
from .webcast_live_analytics_video_detail_response_follower_metric import (
    WebcastLiveAnalyticsVideoDetailResponseFollowerMetric,
)
from .webcast_live_analytics_video_detail_response_interaction import WebcastLiveAnalyticsVideoDetailResponseInteraction
from .webcast_live_analytics_video_detail_response_multi_guest_summary import (
    WebcastLiveAnalyticsVideoDetailResponseMultiGuestSummary,
)
from .webcast_live_analytics_video_detail_response_new_analytics import (
    WebcastLiveAnalyticsVideoDetailResponseNewAnalytics,
)
from .webcast_live_analytics_video_detail_response_new_earnings import (
    WebcastLiveAnalyticsVideoDetailResponseNewEarnings,
)
from .webcast_live_analytics_video_detail_response_new_interaction import (
    WebcastLiveAnalyticsVideoDetailResponseNewInteraction,
)
from .webcast_live_analytics_video_detail_response_new_views import WebcastLiveAnalyticsVideoDetailResponseNewViews
from .webcast_live_analytics_video_detail_response_region_entry import (
    WebcastLiveAnalyticsVideoDetailResponseRegionEntry,
)
from .webcast_live_analytics_video_detail_response_traffic_conversion import (
    WebcastLiveAnalyticsVideoDetailResponseTrafficConversion,
)
from .webcast_live_analytics_video_detail_response_traffic_info import (
    WebcastLiveAnalyticsVideoDetailResponseTrafficInfo,
)
from .webcast_live_analytics_video_detail_response_traffic_total import (
    WebcastLiveAnalyticsVideoDetailResponseTrafficTotal,
)
from .webcast_live_analytics_video_detail_response_video_recomm_info import (
    WebcastLiveAnalyticsVideoDetailResponseVideoRecommInfo,
)
from .webcast_live_analytics_video_detail_response_viewer_info import WebcastLiveAnalyticsVideoDetailResponseViewerInfo
from .webcast_live_analytics_video_detail_response_viewer_portrait import (
    WebcastLiveAnalyticsVideoDetailResponseViewerPortrait,
)
from .webcast_live_analytics_video_detail_response_viewers_age import WebcastLiveAnalyticsVideoDetailResponseViewersAge
from .webcast_live_analytics_video_detail_response_viewers_gender import (
    WebcastLiveAnalyticsVideoDetailResponseViewersGender,
)
from .webcast_live_analytics_video_detail_response_viewers_region import (
    WebcastLiveAnalyticsVideoDetailResponseViewersRegion,
)
from .webcast_live_analytics_video_detail_response_views import WebcastLiveAnalyticsVideoDetailResponseViews
from .webcast_live_analytics_video_detail_response_views_by_section import (
    WebcastLiveAnalyticsVideoDetailResponseViewsBySection,
)
from .webcast_live_analytics_video_detail_response_watcher_rank import (
    WebcastLiveAnalyticsVideoDetailResponseWatcherRank,
)
from .webcast_live_analytics_video_detail_route_output import WebcastLiveAnalyticsVideoDetailRouteOutput
from .webcast_live_analytics_video_list_response import WebcastLiveAnalyticsVideoListResponse
from .webcast_live_analytics_video_list_response_data import WebcastLiveAnalyticsVideoListResponseData
from .webcast_live_analytics_video_list_response_extra import WebcastLiveAnalyticsVideoListResponseExtra
from .webcast_live_analytics_video_list_response_video import WebcastLiveAnalyticsVideoListResponseVideo
from .webcast_live_analytics_video_list_route_output import WebcastLiveAnalyticsVideoListRouteOutput
from .webcast_region_rankings_output import WebcastRegionRankingsOutput
from .webcast_region_rankings_response import WebcastRegionRankingsResponse
from .webcast_room_admin_list_response import WebcastRoomAdminListResponse
from .webcast_room_admin_list_response_admin import WebcastRoomAdminListResponseAdmin
from .webcast_room_admin_list_response_extra import WebcastRoomAdminListResponseExtra
from .webcast_room_admin_list_response_image import WebcastRoomAdminListResponseImage
from .webcast_room_admin_list_route_output import WebcastRoomAdminListRouteOutput
from .webcast_room_admin_update_response import WebcastRoomAdminUpdateResponse
from .webcast_room_admin_update_response_extra import WebcastRoomAdminUpdateResponseExtra
from .webcast_room_admin_update_route_output import WebcastRoomAdminUpdateRouteOutput
from .webcast_room_chat_payload import WebcastRoomChatPayload
from .webcast_room_chat_payload_v1 import WebcastRoomChatPayloadV1
from .webcast_room_chat_route_response import WebcastRoomChatRouteResponse
from .webcast_room_comments_toggle_response import WebcastRoomCommentsToggleResponse
from .webcast_room_comments_toggle_response_extra import WebcastRoomCommentsToggleResponseExtra
from .webcast_room_comments_toggle_route_output import WebcastRoomCommentsToggleRouteOutput
from .webcast_room_id_route_response import WebcastRoomIdRouteResponse
from .webcast_room_info_route_response import WebcastRoomInfoRouteResponse
from .webcast_room_kick_user_response import WebcastRoomKickUserResponse
from .webcast_room_kick_user_response_extra import WebcastRoomKickUserResponseExtra
from .webcast_room_kick_user_route_output import WebcastRoomKickUserRouteOutput
from .webcast_room_kicked_users_response import WebcastRoomKickedUsersResponse
from .webcast_room_kicked_users_response_extra import WebcastRoomKickedUsersResponseExtra
from .webcast_room_kicked_users_route_output import WebcastRoomKickedUsersRouteOutput
from .webcast_room_mute_user_response import WebcastRoomMuteUserResponse
from .webcast_room_mute_user_response_data import WebcastRoomMuteUserResponseData
from .webcast_room_mute_user_response_extra import WebcastRoomMuteUserResponseExtra
from .webcast_room_mute_user_route_output import WebcastRoomMuteUserRouteOutput
from .webcast_room_muted_users_response import WebcastRoomMutedUsersResponse
from .webcast_room_muted_users_response_badge import WebcastRoomMutedUsersResponseBadge
from .webcast_room_muted_users_response_badge_background import WebcastRoomMutedUsersResponseBadgeBackground
from .webcast_room_muted_users_response_badge_combine import WebcastRoomMutedUsersResponseBadgeCombine
from .webcast_room_muted_users_response_badge_text import WebcastRoomMutedUsersResponseBadgeText
from .webcast_room_muted_users_response_enigma_info import WebcastRoomMutedUsersResponseEnigmaInfo
from .webcast_room_muted_users_response_extra import WebcastRoomMutedUsersResponseExtra
from .webcast_room_muted_users_response_follow_info import WebcastRoomMutedUsersResponseFollowInfo
from .webcast_room_muted_users_response_image import WebcastRoomMutedUsersResponseImage
from .webcast_room_muted_users_response_pay_grade import WebcastRoomMutedUsersResponsePayGrade
from .webcast_room_muted_users_response_privilege_log_extra import WebcastRoomMutedUsersResponsePrivilegeLogExtra
from .webcast_room_muted_users_response_user import WebcastRoomMutedUsersResponseUser
from .webcast_room_muted_users_response_user_attr import WebcastRoomMutedUsersResponseUserAttr
from .webcast_room_muted_users_route_output import WebcastRoomMutedUsersRouteOutput
from .webcast_room_unkick_user_response import WebcastRoomUnkickUserResponse
from .webcast_room_unkick_user_response_extra import WebcastRoomUnkickUserResponseExtra
from .webcast_room_unkick_user_route_output import WebcastRoomUnkickUserRouteOutput
from .webcast_room_unmute_user_response import WebcastRoomUnmuteUserResponse
from .webcast_room_unmute_user_response_extra import WebcastRoomUnmuteUserResponseExtra
from .webcast_room_unmute_user_route_output import WebcastRoomUnmuteUserRouteOutput
from .webcast_user_earnings_output import WebcastUserEarningsOutput
from .webcast_user_earnings_output_earnings_estimate_currency_type_1 import (
    WebcastUserEarningsOutputEarningsEstimateCurrencyType1,
)
from .webcast_user_earnings_output_earnings_estimate_currency_type_2_type_1 import (
    WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1,
)
from .webcast_user_earnings_output_earnings_estimate_currency_type_3_type_1 import (
    WebcastUserEarningsOutputEarningsEstimateCurrencyType3Type1,
)
from .webcast_user_earnings_output_period import WebcastUserEarningsOutputPeriod
from .webcast_user_earnings_response import WebcastUserEarningsResponse
from .whirl_captcha_response import WhirlCaptchaResponse
from .whirl_result import WhirlResult

__all__ = (
    "Account",
    "AccountConfig",
    "AccountScopes",
    "AccountsTableRequestLimits",
    "AccountWithPermissionsSafe",
    "Alert",
    "AlertConfig",
    "AlertTarget",
    "AlertTargetConfig",
    "AlertTargetFormat",
    "AlertTargetStatus",
    "ApiKey",
    "ApiKeyConfig",
    "CaptchaCreditsResponse",
    "CompleteIconCaptchaBody",
    "CompletePuzzleCaptchaBody",
    "CompleteShapesCaptchaBody",
    "CompleteWhirlCaptchaBody",
    "CreateAlertBody",
    "CreateAlertResponse",
    "CreateAlertTargetPayload",
    "CreateAlertTargetResponse",
    "CreateJWTResponse",
    "CreateKeyPayload",
    "CreateKeyResponse",
    "DeleteAlertResponse",
    "DeleteAlertTargetResponse",
    "DeleteKeyDeleteBy",
    "DeleteKeyResponse",
    "ExchangeTokenRequest",
    "ExchangeTokenRequestGrantType",
    "GetKeyRetrieveBy",
    "GetRateLimits",
    "GetSignWebcastUrlResponse",
    "HashtagListAPIResponse",
    "HostsResponse",
    "IconCaptchaResponse",
    "IconsResult",
    "JSONResponse",
    "JWTConfig",
    "JWTConfigWebSocketData",
    "JWTCreateConfig",
    "JWTCreateConfigWebSocketData",
    "ListAlertsResponse",
    "ListAlertTargetsResponse",
    "ListKeysResponse",
    "LiveAnalyticsVideoDetailAPIResponse",
    "LiveAnalyticsVideoListAPIResponse",
    "LoadShedInfo",
    "MuteDuration",
    "OAuthRevokeResponse",
    "OAuthScope",
    "OAuthTokenResponse",
    "OxyLabsProxyRegion",
    "PartialSignedUrlInfo",
    "PartialTikTokLiveUserInfo",
    "PartialTikTokUserInfo",
    "PartialWebcastRegionRankingsOutputRank",
    "PartialWebcastRegionRankingsOutputRankUser",
    "PeerPresence",
    "PeerPresenceType",
    "PeerRole",
    "Point",
    "ProxySignResult",
    "PuzzleCaptchaResponse",
    "PuzzleResult",
    "RateLimitInfo",
    "RecordStringAny",
    "RecordStringBooleanOrNumber",
    "RecordStringIsLiveBooleanRoomIdStringOrNull",
    "RecordStringIsLiveBooleanRoomIdStringOrNullAdditionalProperty",
    "RecordStringNumber",
    "RecordStringString",
    "RecordStringUnknown",
    "RetrieveAccountResponse",
    "RetrieveAgentHostsResponse",
    "RetrieveAlertResponse",
    "RetrieveAlertResponseCreator",
    "RetrieveBulkLiveCheckPayload",
    "RetrieveBulkLiveCheckPayloadV1",
    "RetrieveBulkLiveCheckResponse",
    "RetrieveKeyResponse",
    "RetrieveWebcastRankingsRankType",
    "RevokeRequestBody",
    "RevokeRequestBodyTokenTypeHint",
    "RoomAdminUpdateAPIResponse",
    "RoomCommentsToggleAPIResponse",
    "RoomKickedUsersAPIResponse",
    "RoomKickUserAPIResponse",
    "RoomModeratorsAPIResponse",
    "RoomMutedUsersAPIResponse",
    "RoomMuteUserAPIResponse",
    "RoomUnkickUserAPIResponse",
    "RoomUnmuteUserAPIResponse",
    "ShapesCaptchaResponse",
    "ShapesResult",
    "SignTikTokUrlBody",
    "SignTikTokUrlBodyMethod",
    "SignTikTokUrlBodyType",
    "SignTikTokUrlResponse",
    "SoaxProxyRegion",
    "SolveResponseIconsResult",
    "SolveResponsePuzzleResult",
    "SolveResponseShapesResult",
    "SolveResponseWhirlResult",
    "StreamType",
    "TestAlertTargetResponse",
    "TikTokLiveUser",
    "TikTokLiveUserRaw",
    "TikTokLiveUserUser",
    "TokenErrorResponse",
    "TokenResponse",
    "TokenResponseTokenType",
    "Uint8Array",
    "UpdateKeyPayload",
    "UpdateKeyResponse",
    "UpdateKeyUpdateBy",
    "WebcastFeedResponse",
    "WebcastFeedResponseExtra",
    "WebcastFeedResponseExtraLogPb",
    "WebcastFeedResponseHashtag",
    "WebcastFeedResponseHashtagImage",
    "WebcastFeedResponseImage",
    "WebcastFeedResponseItem",
    "WebcastFeedResponseRoomData",
    "WebcastFeedResponseRoomDataBlurredCover",
    "WebcastFeedResponseRoomDataFeedRoomLabel",
    "WebcastFeedResponseRoomDataGameTagDetail",
    "WebcastFeedResponseRoomDataRectangleCoverImg",
    "WebcastFeedResponseRoomDataSquareCoverImg",
    "WebcastFeedResponseRoomDataStats",
    "WebcastFeedResponseRoomDataTaxonomyTagInfo",
    "WebcastFeedResponseStreamUrl",
    "WebcastFeedResponseStreamUrlFlvPullUrl",
    "WebcastFeedResponseStreamUrlLiveCoreSdkData",
    "WebcastFeedResponseStreamUrlLiveCoreSdkDataPullData",
    "WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptions",
    "WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptionsDefaultQuality",
    "WebcastFeedResponseUser",
    "WebcastFeedResponseUserFollowInfo",
    "WebcastFeedResponseUserOwnRoom",
    "WebcastFeedRouteOutput",
    "WebcastFeedRouteResponse",
    "WebcastFetchPlatform",
    "WebcastGiftInfoOutput",
    "WebcastGiftInfoRouteResponse",
    "WebcastHashtagListResponse",
    "WebcastHashtagListResponseData",
    "WebcastHashtagListResponseExtra",
    "WebcastHashtagListResponseGameCategory",
    "WebcastHashtagListResponseGameTag",
    "WebcastHashtagListResponseHashtag",
    "WebcastHashtagListResponseHashtagSimple",
    "WebcastHashtagListResponseImage",
    "WebcastHashtagListRouteOutput",
    "WebcastIsLiveOutput",
    "WebcastLiveAnalyticsVideoDetailResponse",
    "WebcastLiveAnalyticsVideoDetailResponseAnalytics",
    "WebcastLiveAnalyticsVideoDetailResponseAverageWatchTime",
    "WebcastLiveAnalyticsVideoDetailResponseBehaviorSummary",
    "WebcastLiveAnalyticsVideoDetailResponseCohostSummary",
    "WebcastLiveAnalyticsVideoDetailResponseCommentsInfo",
    "WebcastLiveAnalyticsVideoDetailResponseData",
    "WebcastLiveAnalyticsVideoDetailResponseDetailedMetrics",
    "WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails",
    "WebcastLiveAnalyticsVideoDetailResponseEarnings",
    "WebcastLiveAnalyticsVideoDetailResponseExtra",
    "WebcastLiveAnalyticsVideoDetailResponseFollowerMetric",
    "WebcastLiveAnalyticsVideoDetailResponseInteraction",
    "WebcastLiveAnalyticsVideoDetailResponseMultiGuestSummary",
    "WebcastLiveAnalyticsVideoDetailResponseNewAnalytics",
    "WebcastLiveAnalyticsVideoDetailResponseNewEarnings",
    "WebcastLiveAnalyticsVideoDetailResponseNewInteraction",
    "WebcastLiveAnalyticsVideoDetailResponseNewViews",
    "WebcastLiveAnalyticsVideoDetailResponseRegionEntry",
    "WebcastLiveAnalyticsVideoDetailResponseTrafficConversion",
    "WebcastLiveAnalyticsVideoDetailResponseTrafficInfo",
    "WebcastLiveAnalyticsVideoDetailResponseTrafficTotal",
    "WebcastLiveAnalyticsVideoDetailResponseVideoRecommInfo",
    "WebcastLiveAnalyticsVideoDetailResponseViewerInfo",
    "WebcastLiveAnalyticsVideoDetailResponseViewerPortrait",
    "WebcastLiveAnalyticsVideoDetailResponseViewersAge",
    "WebcastLiveAnalyticsVideoDetailResponseViewersGender",
    "WebcastLiveAnalyticsVideoDetailResponseViewersRegion",
    "WebcastLiveAnalyticsVideoDetailResponseViews",
    "WebcastLiveAnalyticsVideoDetailResponseViewsBySection",
    "WebcastLiveAnalyticsVideoDetailResponseWatcherRank",
    "WebcastLiveAnalyticsVideoDetailRouteOutput",
    "WebcastLiveAnalyticsVideoListResponse",
    "WebcastLiveAnalyticsVideoListResponseData",
    "WebcastLiveAnalyticsVideoListResponseExtra",
    "WebcastLiveAnalyticsVideoListResponseVideo",
    "WebcastLiveAnalyticsVideoListRouteOutput",
    "WebcastRegionRankingsOutput",
    "WebcastRegionRankingsResponse",
    "WebcastRoomAdminListResponse",
    "WebcastRoomAdminListResponseAdmin",
    "WebcastRoomAdminListResponseExtra",
    "WebcastRoomAdminListResponseImage",
    "WebcastRoomAdminListRouteOutput",
    "WebcastRoomAdminUpdateResponse",
    "WebcastRoomAdminUpdateResponseExtra",
    "WebcastRoomAdminUpdateRouteOutput",
    "WebcastRoomChatPayload",
    "WebcastRoomChatPayloadV1",
    "WebcastRoomChatRouteResponse",
    "WebcastRoomCommentsToggleResponse",
    "WebcastRoomCommentsToggleResponseExtra",
    "WebcastRoomCommentsToggleRouteOutput",
    "WebcastRoomIdRouteResponse",
    "WebcastRoomInfoRouteResponse",
    "WebcastRoomKickedUsersResponse",
    "WebcastRoomKickedUsersResponseExtra",
    "WebcastRoomKickedUsersRouteOutput",
    "WebcastRoomKickUserResponse",
    "WebcastRoomKickUserResponseExtra",
    "WebcastRoomKickUserRouteOutput",
    "WebcastRoomMutedUsersResponse",
    "WebcastRoomMutedUsersResponseBadge",
    "WebcastRoomMutedUsersResponseBadgeBackground",
    "WebcastRoomMutedUsersResponseBadgeCombine",
    "WebcastRoomMutedUsersResponseBadgeText",
    "WebcastRoomMutedUsersResponseEnigmaInfo",
    "WebcastRoomMutedUsersResponseExtra",
    "WebcastRoomMutedUsersResponseFollowInfo",
    "WebcastRoomMutedUsersResponseImage",
    "WebcastRoomMutedUsersResponsePayGrade",
    "WebcastRoomMutedUsersResponsePrivilegeLogExtra",
    "WebcastRoomMutedUsersResponseUser",
    "WebcastRoomMutedUsersResponseUserAttr",
    "WebcastRoomMutedUsersRouteOutput",
    "WebcastRoomMuteUserResponse",
    "WebcastRoomMuteUserResponseData",
    "WebcastRoomMuteUserResponseExtra",
    "WebcastRoomMuteUserRouteOutput",
    "WebcastRoomUnkickUserResponse",
    "WebcastRoomUnkickUserResponseExtra",
    "WebcastRoomUnkickUserRouteOutput",
    "WebcastRoomUnmuteUserResponse",
    "WebcastRoomUnmuteUserResponseExtra",
    "WebcastRoomUnmuteUserRouteOutput",
    "WebcastUserEarningsOutput",
    "WebcastUserEarningsOutputEarningsEstimateCurrencyType1",
    "WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1",
    "WebcastUserEarningsOutputEarningsEstimateCurrencyType3Type1",
    "WebcastUserEarningsOutputPeriod",
    "WebcastUserEarningsResponse",
    "WhirlCaptchaResponse",
    "WhirlResult",
)
