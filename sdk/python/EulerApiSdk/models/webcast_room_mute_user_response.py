from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_room_mute_user_response_data import WebcastRoomMuteUserResponseData
    from ..models.webcast_room_mute_user_response_extra import WebcastRoomMuteUserResponseExtra


T = TypeVar("T", bound="WebcastRoomMuteUserResponse")


@_attrs_define
class WebcastRoomMuteUserResponse:
    """
    Attributes:
        data (WebcastRoomMuteUserResponseData):
        extra (WebcastRoomMuteUserResponseExtra):
        status_code (float):
    """

    data: WebcastRoomMuteUserResponseData
    extra: WebcastRoomMuteUserResponseExtra
    status_code: float

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        extra = self.extra.to_dict()

        status_code = self.status_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "extra": extra,
                "status_code": status_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_mute_user_response_data import WebcastRoomMuteUserResponseData
        from ..models.webcast_room_mute_user_response_extra import WebcastRoomMuteUserResponseExtra

        d = dict(src_dict)
        data = WebcastRoomMuteUserResponseData.from_dict(d.pop("data"))

        extra = WebcastRoomMuteUserResponseExtra.from_dict(d.pop("extra"))

        status_code = d.pop("status_code")

        webcast_room_mute_user_response = cls(
            data=data,
            extra=extra,
            status_code=status_code,
        )

        return webcast_room_mute_user_response
