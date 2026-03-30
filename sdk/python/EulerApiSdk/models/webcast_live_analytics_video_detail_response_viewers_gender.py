from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewersGender")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewersGender:
    """
    Attributes:
        female_percent (float):
        male_percent (float):
    """

    female_percent: float
    male_percent: float

    def to_dict(self) -> dict[str, Any]:
        female_percent = self.female_percent

        male_percent = self.male_percent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "female_percent": female_percent,
                "male_percent": male_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        female_percent = d.pop("female_percent")

        male_percent = d.pop("male_percent")

        webcast_live_analytics_video_detail_response_viewers_gender = cls(
            female_percent=female_percent,
            male_percent=male_percent,
        )

        return webcast_live_analytics_video_detail_response_viewers_gender
