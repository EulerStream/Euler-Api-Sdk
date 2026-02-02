from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseRegionEntry")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseRegionEntry:
    """
    Attributes:
        percent (float):
        region_name (str):
    """

    percent: float
    region_name: str

    def to_dict(self) -> dict[str, Any]:
        percent = self.percent

        region_name = self.region_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "percent": percent,
                "region_name": region_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percent = d.pop("percent")

        region_name = d.pop("region_name")

        webcast_live_analytics_video_detail_response_region_entry = cls(
            percent=percent,
            region_name=region_name,
        )

        return webcast_live_analytics_video_detail_response_region_entry
