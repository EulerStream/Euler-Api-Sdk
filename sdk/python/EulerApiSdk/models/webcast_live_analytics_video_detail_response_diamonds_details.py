from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails:
    """
    Attributes:
        gift_fan_tickets_percentage (float):
        multi_guest_fan_tickets_percentage (float):
        star_comment_fan_tickets_percentage (float):
        star_comment_qualification (bool):
    """

    gift_fan_tickets_percentage: float
    multi_guest_fan_tickets_percentage: float
    star_comment_fan_tickets_percentage: float
    star_comment_qualification: bool

    def to_dict(self) -> dict[str, Any]:
        gift_fan_tickets_percentage = self.gift_fan_tickets_percentage

        multi_guest_fan_tickets_percentage = self.multi_guest_fan_tickets_percentage

        star_comment_fan_tickets_percentage = self.star_comment_fan_tickets_percentage

        star_comment_qualification = self.star_comment_qualification

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gift_fan_tickets_percentage": gift_fan_tickets_percentage,
                "multi_guest_fan_tickets_percentage": multi_guest_fan_tickets_percentage,
                "star_comment_fan_tickets_percentage": star_comment_fan_tickets_percentage,
                "star_comment_qualification": star_comment_qualification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_fan_tickets_percentage = d.pop("gift_fan_tickets_percentage")

        multi_guest_fan_tickets_percentage = d.pop("multi_guest_fan_tickets_percentage")

        star_comment_fan_tickets_percentage = d.pop("star_comment_fan_tickets_percentage")

        star_comment_qualification = d.pop("star_comment_qualification")

        webcast_live_analytics_video_detail_response_diamonds_details = cls(
            gift_fan_tickets_percentage=gift_fan_tickets_percentage,
            multi_guest_fan_tickets_percentage=multi_guest_fan_tickets_percentage,
            star_comment_fan_tickets_percentage=star_comment_fan_tickets_percentage,
            star_comment_qualification=star_comment_qualification,
        )

        return webcast_live_analytics_video_detail_response_diamonds_details
