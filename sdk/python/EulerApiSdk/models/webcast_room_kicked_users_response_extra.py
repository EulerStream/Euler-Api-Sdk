from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastRoomKickedUsersResponseExtra")


@_attrs_define
class WebcastRoomKickedUsersResponseExtra:
    """
    Attributes:
        has_more (bool):
        next_cursor (float):
        now (float):
        total (float):
    """

    has_more: bool
    next_cursor: float
    now: float
    total: float

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        next_cursor = self.next_cursor

        now = self.now

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "has_more": has_more,
                "next_cursor": next_cursor,
                "now": now,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_more = d.pop("has_more")

        next_cursor = d.pop("next_cursor")

        now = d.pop("now")

        total = d.pop("total")

        webcast_room_kicked_users_response_extra = cls(
            has_more=has_more,
            next_cursor=next_cursor,
            now=now,
            total=total,
        )

        return webcast_room_kicked_users_response_extra
