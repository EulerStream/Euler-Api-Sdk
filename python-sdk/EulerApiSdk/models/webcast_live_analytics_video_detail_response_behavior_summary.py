from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_cohost_summary import (
        WebcastLiveAnalyticsVideoDetailResponseCohostSummary,
    )
    from ..models.webcast_live_analytics_video_detail_response_multi_guest_summary import (
        WebcastLiveAnalyticsVideoDetailResponseMultiGuestSummary,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseBehaviorSummary")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseBehaviorSummary:
    """
    Attributes:
        cohost_summary (WebcastLiveAnalyticsVideoDetailResponseCohostSummary):
        multi_guest_summary (WebcastLiveAnalyticsVideoDetailResponseMultiGuestSummary):
    """

    cohost_summary: WebcastLiveAnalyticsVideoDetailResponseCohostSummary
    multi_guest_summary: WebcastLiveAnalyticsVideoDetailResponseMultiGuestSummary

    def to_dict(self) -> dict[str, Any]:
        cohost_summary = self.cohost_summary.to_dict()

        multi_guest_summary = self.multi_guest_summary.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cohost_summary": cohost_summary,
                "multi_guest_summary": multi_guest_summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_cohost_summary import (
            WebcastLiveAnalyticsVideoDetailResponseCohostSummary,
        )
        from ..models.webcast_live_analytics_video_detail_response_multi_guest_summary import (
            WebcastLiveAnalyticsVideoDetailResponseMultiGuestSummary,
        )

        d = dict(src_dict)
        cohost_summary = WebcastLiveAnalyticsVideoDetailResponseCohostSummary.from_dict(d.pop("cohost_summary"))

        multi_guest_summary = WebcastLiveAnalyticsVideoDetailResponseMultiGuestSummary.from_dict(
            d.pop("multi_guest_summary")
        )

        webcast_live_analytics_video_detail_response_behavior_summary = cls(
            cohost_summary=cohost_summary,
            multi_guest_summary=multi_guest_summary,
        )

        return webcast_live_analytics_video_detail_response_behavior_summary
