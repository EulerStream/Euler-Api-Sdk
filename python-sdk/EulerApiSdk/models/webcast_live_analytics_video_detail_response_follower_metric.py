from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseFollowerMetric")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseFollowerMetric:
    """
    Attributes:
        follower (float):
        non_follower (float):
    """

    follower: float
    non_follower: float

    def to_dict(self) -> dict[str, Any]:
        follower = self.follower

        non_follower = self.non_follower

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "follower": follower,
                "non_follower": non_follower,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        follower = d.pop("follower")

        non_follower = d.pop("non_follower")

        webcast_live_analytics_video_detail_response_follower_metric = cls(
            follower=follower,
            non_follower=non_follower,
        )

        return webcast_live_analytics_video_detail_response_follower_metric
