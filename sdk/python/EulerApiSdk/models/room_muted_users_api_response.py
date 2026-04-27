from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webcast_room_muted_users_route_output import WebcastRoomMutedUsersRouteOutput


T = TypeVar("T", bound="RoomMutedUsersAPIResponse")


@_attrs_define
class RoomMutedUsersAPIResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        response (WebcastRoomMutedUsersRouteOutput | Unset):
    """

    code: float
    message: str | Unset = UNSET
    response: WebcastRoomMutedUsersRouteOutput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_muted_users_route_output import WebcastRoomMutedUsersRouteOutput

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _response = d.pop("response", UNSET)
        response: WebcastRoomMutedUsersRouteOutput | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = WebcastRoomMutedUsersRouteOutput.from_dict(_response)

        room_muted_users_api_response = cls(
            code=code,
            message=message,
            response=response,
        )

        return room_muted_users_api_response
