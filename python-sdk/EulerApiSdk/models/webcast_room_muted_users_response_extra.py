from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastRoomMutedUsersResponseExtra")


@_attrs_define
class WebcastRoomMutedUsersResponseExtra:
    """
    Attributes:
        datas (list[Any]):
        has_more (bool):
        max_count (float):
        next_cursor (float):
        now (float):
        total (float):
    """

    datas: list[Any]
    has_more: bool
    max_count: float
    next_cursor: float
    now: float
    total: float

    def to_dict(self) -> dict[str, Any]:
        datas = self.datas

        has_more = self.has_more

        max_count = self.max_count

        next_cursor = self.next_cursor

        now = self.now

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "datas": datas,
                "has_more": has_more,
                "max_count": max_count,
                "next_cursor": next_cursor,
                "now": now,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        datas = cast(list[Any], d.pop("datas"))

        has_more = d.pop("has_more")

        max_count = d.pop("max_count")

        next_cursor = d.pop("next_cursor")

        now = d.pop("now")

        total = d.pop("total")

        webcast_room_muted_users_response_extra = cls(
            datas=datas,
            has_more=has_more,
            max_count=max_count,
            next_cursor=next_cursor,
            now=now,
            total=total,
        )

        return webcast_room_muted_users_response_extra
