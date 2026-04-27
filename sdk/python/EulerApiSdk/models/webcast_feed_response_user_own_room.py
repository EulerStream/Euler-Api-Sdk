from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastFeedResponseUserOwnRoom")


@_attrs_define
class WebcastFeedResponseUserOwnRoom:
    """
    Attributes:
        room_ids_str (list[str]):
        room_ids (list[float]):
    """

    room_ids_str: list[str]
    room_ids: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        room_ids_str = self.room_ids_str

        room_ids = self.room_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "room_ids_str": room_ids_str,
                "room_ids": room_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_ids_str = cast(list[str], d.pop("room_ids_str"))

        room_ids = cast(list[float], d.pop("room_ids"))

        webcast_feed_response_user_own_room = cls(
            room_ids_str=room_ids_str,
            room_ids=room_ids,
        )

        webcast_feed_response_user_own_room.additional_properties = d
        return webcast_feed_response_user_own_room

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
