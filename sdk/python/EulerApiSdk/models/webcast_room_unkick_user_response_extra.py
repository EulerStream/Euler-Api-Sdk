from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastRoomUnkickUserResponseExtra")


@_attrs_define
class WebcastRoomUnkickUserResponseExtra:
    """
    Attributes:
        now (float):
    """

    now: float

    def to_dict(self) -> dict[str, Any]:
        now = self.now

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "now": now,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        now = d.pop("now")

        webcast_room_unkick_user_response_extra = cls(
            now=now,
        )

        return webcast_room_unkick_user_response_extra
