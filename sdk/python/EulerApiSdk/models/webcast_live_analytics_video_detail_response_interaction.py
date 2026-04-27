from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseInteraction")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseInteraction:
    """
    Attributes:
        comment (float):
        likes (float):
        new_followers (float):
        shares (float):
    """

    comment: float
    likes: float
    new_followers: float
    shares: float

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        likes = self.likes

        new_followers = self.new_followers

        shares = self.shares

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "comment": comment,
                "likes": likes,
                "new_followers": new_followers,
                "shares": shares,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        likes = d.pop("likes")

        new_followers = d.pop("new_followers")

        shares = d.pop("shares")

        webcast_live_analytics_video_detail_response_interaction = cls(
            comment=comment,
            likes=likes,
            new_followers=new_followers,
            shares=shares,
        )

        return webcast_live_analytics_video_detail_response_interaction
