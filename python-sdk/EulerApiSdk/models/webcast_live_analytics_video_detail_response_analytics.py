from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_earnings import (
        WebcastLiveAnalyticsVideoDetailResponseEarnings,
    )
    from ..models.webcast_live_analytics_video_detail_response_interaction import (
        WebcastLiveAnalyticsVideoDetailResponseInteraction,
    )
    from ..models.webcast_live_analytics_video_detail_response_views import WebcastLiveAnalyticsVideoDetailResponseViews


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseAnalytics")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseAnalytics:
    """
    Attributes:
        earnings (WebcastLiveAnalyticsVideoDetailResponseEarnings):
        interaction (WebcastLiveAnalyticsVideoDetailResponseInteraction):
        views (WebcastLiveAnalyticsVideoDetailResponseViews):
    """

    earnings: WebcastLiveAnalyticsVideoDetailResponseEarnings
    interaction: WebcastLiveAnalyticsVideoDetailResponseInteraction
    views: WebcastLiveAnalyticsVideoDetailResponseViews

    def to_dict(self) -> dict[str, Any]:
        earnings = self.earnings.to_dict()

        interaction = self.interaction.to_dict()

        views = self.views.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "earnings": earnings,
                "interaction": interaction,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_earnings import (
            WebcastLiveAnalyticsVideoDetailResponseEarnings,
        )
        from ..models.webcast_live_analytics_video_detail_response_interaction import (
            WebcastLiveAnalyticsVideoDetailResponseInteraction,
        )
        from ..models.webcast_live_analytics_video_detail_response_views import (
            WebcastLiveAnalyticsVideoDetailResponseViews,
        )

        d = dict(src_dict)
        earnings = WebcastLiveAnalyticsVideoDetailResponseEarnings.from_dict(d.pop("earnings"))

        interaction = WebcastLiveAnalyticsVideoDetailResponseInteraction.from_dict(d.pop("interaction"))

        views = WebcastLiveAnalyticsVideoDetailResponseViews.from_dict(d.pop("views"))

        webcast_live_analytics_video_detail_response_analytics = cls(
            earnings=earnings,
            interaction=interaction,
            views=views,
        )

        return webcast_live_analytics_video_detail_response_analytics
