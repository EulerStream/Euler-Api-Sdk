from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_viewer_portrait import (
        WebcastLiveAnalyticsVideoDetailResponseViewerPortrait,
    )
    from ..models.webcast_live_analytics_video_detail_response_watcher_rank import (
        WebcastLiveAnalyticsVideoDetailResponseWatcherRank,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewerInfo")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewerInfo:
    """
    Attributes:
        gift_rank (list[Any]):
        viewer_portrait (WebcastLiveAnalyticsVideoDetailResponseViewerPortrait):
        watcher_rank (list[WebcastLiveAnalyticsVideoDetailResponseWatcherRank]):
    """

    gift_rank: list[Any]
    viewer_portrait: WebcastLiveAnalyticsVideoDetailResponseViewerPortrait
    watcher_rank: list[WebcastLiveAnalyticsVideoDetailResponseWatcherRank]

    def to_dict(self) -> dict[str, Any]:
        gift_rank = self.gift_rank

        viewer_portrait = self.viewer_portrait.to_dict()

        watcher_rank = []
        for watcher_rank_item_data in self.watcher_rank:
            watcher_rank_item = watcher_rank_item_data.to_dict()
            watcher_rank.append(watcher_rank_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gift_rank": gift_rank,
                "viewer_portrait": viewer_portrait,
                "watcher_rank": watcher_rank,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_viewer_portrait import (
            WebcastLiveAnalyticsVideoDetailResponseViewerPortrait,
        )
        from ..models.webcast_live_analytics_video_detail_response_watcher_rank import (
            WebcastLiveAnalyticsVideoDetailResponseWatcherRank,
        )

        d = dict(src_dict)
        gift_rank = cast(list[Any], d.pop("gift_rank"))

        viewer_portrait = WebcastLiveAnalyticsVideoDetailResponseViewerPortrait.from_dict(d.pop("viewer_portrait"))

        watcher_rank = []
        _watcher_rank = d.pop("watcher_rank")
        for watcher_rank_item_data in _watcher_rank:
            watcher_rank_item = WebcastLiveAnalyticsVideoDetailResponseWatcherRank.from_dict(watcher_rank_item_data)

            watcher_rank.append(watcher_rank_item)

        webcast_live_analytics_video_detail_response_viewer_info = cls(
            gift_rank=gift_rank,
            viewer_portrait=viewer_portrait,
            watcher_rank=watcher_rank,
        )

        return webcast_live_analytics_video_detail_response_viewer_info
