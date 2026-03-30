from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoListResponseVideo")


@_attrs_define
class WebcastLiveAnalyticsVideoListResponseVideo:
    """
    Attributes:
        cover (str):
        diamonds (float):
        duration (float):
        end_time (float):
        new_followers (float):
        room_id (str):
        start_time (float):
        title (str):
        views (float):
    """

    cover: str
    diamonds: float
    duration: float
    end_time: float
    new_followers: float
    room_id: str
    start_time: float
    title: str
    views: float

    def to_dict(self) -> dict[str, Any]:
        cover = self.cover

        diamonds = self.diamonds

        duration = self.duration

        end_time = self.end_time

        new_followers = self.new_followers

        room_id = self.room_id

        start_time = self.start_time

        title = self.title

        views = self.views

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cover": cover,
                "diamonds": diamonds,
                "duration": duration,
                "end_time": end_time,
                "new_followers": new_followers,
                "room_id": room_id,
                "start_time": start_time,
                "title": title,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cover = d.pop("cover")

        diamonds = d.pop("diamonds")

        duration = d.pop("duration")

        end_time = d.pop("end_time")

        new_followers = d.pop("new_followers")

        room_id = d.pop("room_id")

        start_time = d.pop("start_time")

        title = d.pop("title")

        views = d.pop("views")

        webcast_live_analytics_video_list_response_video = cls(
            cover=cover,
            diamonds=diamonds,
            duration=duration,
            end_time=end_time,
            new_followers=new_followers,
            room_id=room_id,
            start_time=start_time,
            title=title,
            views=views,
        )

        return webcast_live_analytics_video_list_response_video
