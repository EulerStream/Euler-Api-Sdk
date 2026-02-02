from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_list_response_video import WebcastLiveAnalyticsVideoListResponseVideo


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoListResponseData")


@_attrs_define
class WebcastLiveAnalyticsVideoListResponseData:
    """
    Attributes:
        total (float):
        video_list (list[WebcastLiveAnalyticsVideoListResponseVideo]):
    """

    total: float
    video_list: list[WebcastLiveAnalyticsVideoListResponseVideo]

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        video_list = []
        for video_list_item_data in self.video_list:
            video_list_item = video_list_item_data.to_dict()
            video_list.append(video_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "video_list": video_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_list_response_video import WebcastLiveAnalyticsVideoListResponseVideo

        d = dict(src_dict)
        total = d.pop("total")

        video_list = []
        _video_list = d.pop("video_list")
        for video_list_item_data in _video_list:
            video_list_item = WebcastLiveAnalyticsVideoListResponseVideo.from_dict(video_list_item_data)

            video_list.append(video_list_item)

        webcast_live_analytics_video_list_response_data = cls(
            total=total,
            video_list=video_list,
        )

        return webcast_live_analytics_video_list_response_data
