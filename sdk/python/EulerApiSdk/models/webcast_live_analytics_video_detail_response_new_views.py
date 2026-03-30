from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseNewViews")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseNewViews:
    """
    Attributes:
        anchor_live_acu (float):
        average_watch_time (float):
        last_anchor_live_acu (float):
        last_average_watch_time (float):
        last_three_min_total_views (float):
        last_top_viewer_count (float):
        last_total_views (float):
        last_unique_viewers (float):
        three_min_total_views (float):
        top_viewer_count (float):
        total_views (float):
        unique_viewers (float):
    """

    anchor_live_acu: float
    average_watch_time: float
    last_anchor_live_acu: float
    last_average_watch_time: float
    last_three_min_total_views: float
    last_top_viewer_count: float
    last_total_views: float
    last_unique_viewers: float
    three_min_total_views: float
    top_viewer_count: float
    total_views: float
    unique_viewers: float

    def to_dict(self) -> dict[str, Any]:
        anchor_live_acu = self.anchor_live_acu

        average_watch_time = self.average_watch_time

        last_anchor_live_acu = self.last_anchor_live_acu

        last_average_watch_time = self.last_average_watch_time

        last_three_min_total_views = self.last_three_min_total_views

        last_top_viewer_count = self.last_top_viewer_count

        last_total_views = self.last_total_views

        last_unique_viewers = self.last_unique_viewers

        three_min_total_views = self.three_min_total_views

        top_viewer_count = self.top_viewer_count

        total_views = self.total_views

        unique_viewers = self.unique_viewers

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "anchor_live_acu": anchor_live_acu,
                "average_watch_time": average_watch_time,
                "last_anchor_live_acu": last_anchor_live_acu,
                "last_average_watch_time": last_average_watch_time,
                "last_three_min_total_views": last_three_min_total_views,
                "last_top_viewer_count": last_top_viewer_count,
                "last_total_views": last_total_views,
                "last_unique_viewers": last_unique_viewers,
                "three_min_total_views": three_min_total_views,
                "top_viewer_count": top_viewer_count,
                "total_views": total_views,
                "unique_viewers": unique_viewers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        anchor_live_acu = d.pop("anchor_live_acu")

        average_watch_time = d.pop("average_watch_time")

        last_anchor_live_acu = d.pop("last_anchor_live_acu")

        last_average_watch_time = d.pop("last_average_watch_time")

        last_three_min_total_views = d.pop("last_three_min_total_views")

        last_top_viewer_count = d.pop("last_top_viewer_count")

        last_total_views = d.pop("last_total_views")

        last_unique_viewers = d.pop("last_unique_viewers")

        three_min_total_views = d.pop("three_min_total_views")

        top_viewer_count = d.pop("top_viewer_count")

        total_views = d.pop("total_views")

        unique_viewers = d.pop("unique_viewers")

        webcast_live_analytics_video_detail_response_new_views = cls(
            anchor_live_acu=anchor_live_acu,
            average_watch_time=average_watch_time,
            last_anchor_live_acu=last_anchor_live_acu,
            last_average_watch_time=last_average_watch_time,
            last_three_min_total_views=last_three_min_total_views,
            last_top_viewer_count=last_top_viewer_count,
            last_total_views=last_total_views,
            last_unique_viewers=last_unique_viewers,
            three_min_total_views=three_min_total_views,
            top_viewer_count=top_viewer_count,
            total_views=total_views,
            unique_viewers=unique_viewers,
        )

        return webcast_live_analytics_video_detail_response_new_views
