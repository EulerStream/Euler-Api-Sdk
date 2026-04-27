from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseVideoRecommInfo")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseVideoRecommInfo:
    """
    Attributes:
        total_views (float):
        video_info (list[Any]):
    """

    total_views: float
    video_info: list[Any]

    def to_dict(self) -> dict[str, Any]:
        total_views = self.total_views

        video_info = self.video_info

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total_views": total_views,
                "video_info": video_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_views = d.pop("total_views")

        video_info = cast(list[Any], d.pop("video_info"))

        webcast_live_analytics_video_detail_response_video_recomm_info = cls(
            total_views=total_views,
            video_info=video_info,
        )

        return webcast_live_analytics_video_detail_response_video_recomm_info
