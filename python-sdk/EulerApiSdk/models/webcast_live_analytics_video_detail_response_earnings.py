from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_diamonds_details import (
        WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseEarnings")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseEarnings:
    """
    Attributes:
        diamonds (float):
        diamonds_details (WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails):
        gifters (float):
    """

    diamonds: float
    diamonds_details: WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails
    gifters: float

    def to_dict(self) -> dict[str, Any]:
        diamonds = self.diamonds

        diamonds_details = self.diamonds_details.to_dict()

        gifters = self.gifters

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "diamonds": diamonds,
                "diamonds_details": diamonds_details,
                "gifters": gifters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_diamonds_details import (
            WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails,
        )

        d = dict(src_dict)
        diamonds = d.pop("diamonds")

        diamonds_details = WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails.from_dict(d.pop("diamonds_details"))

        gifters = d.pop("gifters")

        webcast_live_analytics_video_detail_response_earnings = cls(
            diamonds=diamonds,
            diamonds_details=diamonds_details,
            gifters=gifters,
        )

        return webcast_live_analytics_video_detail_response_earnings
