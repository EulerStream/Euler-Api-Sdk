from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_region_entry import (
        WebcastLiveAnalyticsVideoDetailResponseRegionEntry,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewersRegion")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewersRegion:
    """
    Attributes:
        others (float):
        top_viewers_region_list (list[WebcastLiveAnalyticsVideoDetailResponseRegionEntry]):
    """

    others: float
    top_viewers_region_list: list[WebcastLiveAnalyticsVideoDetailResponseRegionEntry]

    def to_dict(self) -> dict[str, Any]:
        others = self.others

        top_viewers_region_list = []
        for top_viewers_region_list_item_data in self.top_viewers_region_list:
            top_viewers_region_list_item = top_viewers_region_list_item_data.to_dict()
            top_viewers_region_list.append(top_viewers_region_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "others": others,
                "top_viewers_region_list": top_viewers_region_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_region_entry import (
            WebcastLiveAnalyticsVideoDetailResponseRegionEntry,
        )

        d = dict(src_dict)
        others = d.pop("others")

        top_viewers_region_list = []
        _top_viewers_region_list = d.pop("top_viewers_region_list")
        for top_viewers_region_list_item_data in _top_viewers_region_list:
            top_viewers_region_list_item = WebcastLiveAnalyticsVideoDetailResponseRegionEntry.from_dict(
                top_viewers_region_list_item_data
            )

            top_viewers_region_list.append(top_viewers_region_list_item)

        webcast_live_analytics_video_detail_response_viewers_region = cls(
            others=others,
            top_viewers_region_list=top_viewers_region_list,
        )

        return webcast_live_analytics_video_detail_response_viewers_region
