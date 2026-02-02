from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_room_muted_users_response_extra import WebcastRoomMutedUsersResponseExtra
    from ..models.webcast_room_muted_users_response_user import WebcastRoomMutedUsersResponseUser


T = TypeVar("T", bound="WebcastRoomMutedUsersResponse")


@_attrs_define
class WebcastRoomMutedUsersResponse:
    """
    Attributes:
        data (list[WebcastRoomMutedUsersResponseUser]):
        extra (WebcastRoomMutedUsersResponseExtra):
        status_code (float):
    """

    data: list[WebcastRoomMutedUsersResponseUser]
    extra: WebcastRoomMutedUsersResponseExtra
    status_code: float

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

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
        from ..models.webcast_room_muted_users_response_extra import WebcastRoomMutedUsersResponseExtra
        from ..models.webcast_room_muted_users_response_user import WebcastRoomMutedUsersResponseUser

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = WebcastRoomMutedUsersResponseUser.from_dict(data_item_data)

            data.append(data_item)

        extra = WebcastRoomMutedUsersResponseExtra.from_dict(d.pop("extra"))

        status_code = d.pop("status_code")

        webcast_room_muted_users_response = cls(
            data=data,
            extra=extra,
            status_code=status_code,
        )

        return webcast_room_muted_users_response
