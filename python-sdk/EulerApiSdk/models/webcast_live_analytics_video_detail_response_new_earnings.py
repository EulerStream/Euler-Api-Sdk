from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_diamonds_details import (
        WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseNewEarnings")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseNewEarnings:
    """
    Attributes:
        diamonds (float):
        diamonds_details (WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails):
        last_diamonds (float):
    """

    diamonds: float
    diamonds_details: WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails
    last_diamonds: float

    def to_dict(self) -> dict[str, Any]:
        diamonds = self.diamonds

        diamonds_details = self.diamonds_details.to_dict()

        last_diamonds = self.last_diamonds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "diamonds": diamonds,
                "diamonds_details": diamonds_details,
                "last_diamonds": last_diamonds,
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

        last_diamonds = d.pop("last_diamonds")

        webcast_live_analytics_video_detail_response_new_earnings = cls(
            diamonds=diamonds,
            diamonds_details=diamonds_details,
            last_diamonds=last_diamonds,
        )

        return webcast_live_analytics_video_detail_response_new_earnings
