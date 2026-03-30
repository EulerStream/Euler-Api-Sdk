from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebcastRoomIdRouteResponse")


@_attrs_define
class WebcastRoomIdRouteResponse:
    """
    Attributes:
        code (float):
        ok (bool):
        routes_attempted (list[str]):
        message (str | Unset):
        is_live (bool | Unset):
        room_id (str | Unset):
    """

    code: float
    ok: bool
    routes_attempted: list[str]
    message: str | Unset = UNSET
    is_live: bool | Unset = UNSET
    room_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        ok = self.ok

        routes_attempted = self.routes_attempted

        message = self.message

        is_live = self.is_live

        room_id = self.room_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "ok": ok,
                "routes_attempted": routes_attempted,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if is_live is not UNSET:
            field_dict["is_live"] = is_live
        if room_id is not UNSET:
            field_dict["room_id"] = room_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        ok = d.pop("ok")

        routes_attempted = cast(list[str], d.pop("routes_attempted"))

        message = d.pop("message", UNSET)

        is_live = d.pop("is_live", UNSET)

        room_id = d.pop("room_id", UNSET)

        webcast_room_id_route_response = cls(
            code=code,
            ok=ok,
            routes_attempted=routes_attempted,
            message=message,
            is_live=is_live,
            room_id=room_id,
        )

        return webcast_room_id_route_response
