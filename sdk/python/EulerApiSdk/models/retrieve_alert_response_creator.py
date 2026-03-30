from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RetrieveAlertResponseCreator")


@_attrs_define
class RetrieveAlertResponseCreator:
    """
    Attributes:
        last_nickname (None | str):
        last_avatar_url (None | str):
        room_id (None | str):
        state_label (str):
        state (float):
        unique_id (str):
    """

    last_nickname: None | str
    last_avatar_url: None | str
    room_id: None | str
    state_label: str
    state: float
    unique_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_nickname: None | str
        last_nickname = self.last_nickname

        last_avatar_url: None | str
        last_avatar_url = self.last_avatar_url

        room_id: None | str
        room_id = self.room_id

        state_label = self.state_label

        state = self.state

        unique_id = self.unique_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_nickname": last_nickname,
                "last_avatar_url": last_avatar_url,
                "room_id": room_id,
                "state_label": state_label,
                "state": state,
                "unique_id": unique_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_last_nickname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_nickname = _parse_last_nickname(d.pop("last_nickname"))

        def _parse_last_avatar_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_avatar_url = _parse_last_avatar_url(d.pop("last_avatar_url"))

        def _parse_room_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        room_id = _parse_room_id(d.pop("room_id"))

        state_label = d.pop("state_label")

        state = d.pop("state")

        unique_id = d.pop("unique_id")

        retrieve_alert_response_creator = cls(
            last_nickname=last_nickname,
            last_avatar_url=last_avatar_url,
            room_id=room_id,
            state_label=state_label,
            state=state,
            unique_id=unique_id,
        )

        retrieve_alert_response_creator.additional_properties = d
        return retrieve_alert_response_creator

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
