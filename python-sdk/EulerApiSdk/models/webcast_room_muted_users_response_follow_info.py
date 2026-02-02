from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastRoomMutedUsersResponseFollowInfo")


@_attrs_define
class WebcastRoomMutedUsersResponseFollowInfo:
    """
    Attributes:
        follow_status (float):
        follower_count (float):
        following_count (float):
        push_status (float):
    """

    follow_status: float
    follower_count: float
    following_count: float
    push_status: float

    def to_dict(self) -> dict[str, Any]:
        follow_status = self.follow_status

        follower_count = self.follower_count

        following_count = self.following_count

        push_status = self.push_status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "follow_status": follow_status,
                "follower_count": follower_count,
                "following_count": following_count,
                "push_status": push_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        follow_status = d.pop("follow_status")

        follower_count = d.pop("follower_count")

        following_count = d.pop("following_count")

        push_status = d.pop("push_status")

        webcast_room_muted_users_response_follow_info = cls(
            follow_status=follow_status,
            follower_count=follower_count,
            following_count=following_count,
            push_status=push_status,
        )

        return webcast_room_muted_users_response_follow_info
