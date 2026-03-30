from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_new_earnings import (
        WebcastLiveAnalyticsVideoDetailResponseNewEarnings,
    )
    from ..models.webcast_live_analytics_video_detail_response_new_interaction import (
        WebcastLiveAnalyticsVideoDetailResponseNewInteraction,
    )
    from ..models.webcast_live_analytics_video_detail_response_new_views import (
        WebcastLiveAnalyticsVideoDetailResponseNewViews,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseNewAnalytics")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseNewAnalytics:
    """
    Attributes:
        earnings (WebcastLiveAnalyticsVideoDetailResponseNewEarnings):
        interaction (WebcastLiveAnalyticsVideoDetailResponseNewInteraction):
        views (WebcastLiveAnalyticsVideoDetailResponseNewViews):
    """

    earnings: WebcastLiveAnalyticsVideoDetailResponseNewEarnings
    interaction: WebcastLiveAnalyticsVideoDetailResponseNewInteraction
    views: WebcastLiveAnalyticsVideoDetailResponseNewViews

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
        from ..models.webcast_live_analytics_video_detail_response_new_earnings import (
            WebcastLiveAnalyticsVideoDetailResponseNewEarnings,
        )
        from ..models.webcast_live_analytics_video_detail_response_new_interaction import (
            WebcastLiveAnalyticsVideoDetailResponseNewInteraction,
        )
        from ..models.webcast_live_analytics_video_detail_response_new_views import (
            WebcastLiveAnalyticsVideoDetailResponseNewViews,
        )

        d = dict(src_dict)
        earnings = WebcastLiveAnalyticsVideoDetailResponseNewEarnings.from_dict(d.pop("earnings"))

        interaction = WebcastLiveAnalyticsVideoDetailResponseNewInteraction.from_dict(d.pop("interaction"))

        views = WebcastLiveAnalyticsVideoDetailResponseNewViews.from_dict(d.pop("views"))

        webcast_live_analytics_video_detail_response_new_analytics = cls(
            earnings=earnings,
            interaction=interaction,
            views=views,
        )

        return webcast_live_analytics_video_detail_response_new_analytics
