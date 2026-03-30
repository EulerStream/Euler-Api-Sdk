from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebcastRoomChatRouteResponse")


@_attrs_define
class WebcastRoomChatRouteResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        data (Any | Unset):
    """

    code: float
    message: str | Unset = UNSET
    data: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        data = d.pop("data", UNSET)

        webcast_room_chat_route_response = cls(
            code=code,
            message=message,
            data=data,
        )

        return webcast_room_chat_route_response
