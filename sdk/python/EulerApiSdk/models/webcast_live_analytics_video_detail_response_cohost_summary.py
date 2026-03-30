from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseCohostSummary")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseCohostSummary:
    """
    Attributes:
        cohost_rank (list[Any]):
        total_anchor (float):
        total_diamonds (float):
        total_views (float):
    """

    cohost_rank: list[Any]
    total_anchor: float
    total_diamonds: float
    total_views: float

    def to_dict(self) -> dict[str, Any]:
        cohost_rank = self.cohost_rank

        total_anchor = self.total_anchor

        total_diamonds = self.total_diamonds

        total_views = self.total_views

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cohost_rank": cohost_rank,
                "total_anchor": total_anchor,
                "total_diamonds": total_diamonds,
                "total_views": total_views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cohost_rank = cast(list[Any], d.pop("cohost_rank"))

        total_anchor = d.pop("total_anchor")

        total_diamonds = d.pop("total_diamonds")

        total_views = d.pop("total_views")

        webcast_live_analytics_video_detail_response_cohost_summary = cls(
            cohost_rank=cohost_rank,
            total_anchor=total_anchor,
            total_diamonds=total_diamonds,
            total_views=total_views,
        )

        return webcast_live_analytics_video_detail_response_cohost_summary
