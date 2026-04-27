from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastRoomMutedUsersResponseEnigmaInfo")


@_attrs_define
class WebcastRoomMutedUsersResponseEnigmaInfo:
    """
    Attributes:
        is_enigma_mask_on (bool):
    """

    is_enigma_mask_on: bool

    def to_dict(self) -> dict[str, Any]:
        is_enigma_mask_on = self.is_enigma_mask_on

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "is_enigma_mask_on": is_enigma_mask_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enigma_mask_on = d.pop("is_enigma_mask_on")

        webcast_room_muted_users_response_enigma_info = cls(
            is_enigma_mask_on=is_enigma_mask_on,
        )

        return webcast_room_muted_users_response_enigma_info
