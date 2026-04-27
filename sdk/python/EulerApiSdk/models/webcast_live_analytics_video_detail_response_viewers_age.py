from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewersAge")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewersAge:
    """
    Attributes:
        age_section (str):
        percent (float):
    """

    age_section: str
    percent: float

    def to_dict(self) -> dict[str, Any]:
        age_section = self.age_section

        percent = self.percent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "age_section": age_section,
                "percent": percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        age_section = d.pop("age_section")

        percent = d.pop("percent")

        webcast_live_analytics_video_detail_response_viewers_age = cls(
            age_section=age_section,
            percent=percent,
        )

        return webcast_live_analytics_video_detail_response_viewers_age
