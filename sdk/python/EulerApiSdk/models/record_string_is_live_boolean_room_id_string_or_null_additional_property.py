from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecordStringIsLiveBooleanRoomIdStringOrNullAdditionalProperty")


@_attrs_define
class RecordStringIsLiveBooleanRoomIdStringOrNullAdditionalProperty:
    """
    Attributes:
        room_id (str):
        is_live (bool):
    """

    room_id: str
    is_live: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        room_id = self.room_id

        is_live = self.is_live

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "room_id": room_id,
                "is_live": is_live,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_id = d.pop("room_id")

        is_live = d.pop("is_live")

        record_string_is_live_boolean_room_id_string_or_null_additional_property = cls(
            room_id=room_id,
            is_live=is_live,
        )

        record_string_is_live_boolean_room_id_string_or_null_additional_property.additional_properties = d
        return record_string_is_live_boolean_room_id_string_or_null_additional_property

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
