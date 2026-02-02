from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseTrafficConversion")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseTrafficConversion:
    """
    Attributes:
        gifters (float):
        impression_viewers (float):
        unique_viewers (float):
    """

    gifters: float
    impression_viewers: float
    unique_viewers: float

    def to_dict(self) -> dict[str, Any]:
        gifters = self.gifters

        impression_viewers = self.impression_viewers

        unique_viewers = self.unique_viewers

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gifters": gifters,
                "impression_viewers": impression_viewers,
                "unique_viewers": unique_viewers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gifters = d.pop("gifters")

        impression_viewers = d.pop("impression_viewers")

        unique_viewers = d.pop("unique_viewers")

        webcast_live_analytics_video_detail_response_traffic_conversion = cls(
            gifters=gifters,
            impression_viewers=impression_viewers,
            unique_viewers=unique_viewers,
        )

        return webcast_live_analytics_video_detail_response_traffic_conversion
