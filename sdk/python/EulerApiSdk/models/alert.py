from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """
    Attributes:
        account_id (float):
        alert_creator_id (float):
        read_only (bool):
        alert_creator_nickname (None | str):
        alert_creator_avatar_url (None | str):
        alert_creator_username (str):
        created_at (datetime.datetime):
        id (float):
    """

    account_id: float
    alert_creator_id: float
    read_only: bool
    alert_creator_nickname: None | str
    alert_creator_avatar_url: None | str
    alert_creator_username: str
    created_at: datetime.datetime
    id: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        alert_creator_id = self.alert_creator_id

        read_only = self.read_only

        alert_creator_nickname: None | str
        alert_creator_nickname = self.alert_creator_nickname

        alert_creator_avatar_url: None | str
        alert_creator_avatar_url = self.alert_creator_avatar_url

        alert_creator_username = self.alert_creator_username

        created_at = self.created_at.isoformat()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "alert_creator_id": alert_creator_id,
                "read_only": read_only,
                "alert_creator_nickname": alert_creator_nickname,
                "alert_creator_avatar_url": alert_creator_avatar_url,
                "alert_creator_username": alert_creator_username,
                "created_at": created_at,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        alert_creator_id = d.pop("alert_creator_id")

        read_only = d.pop("read_only")

        def _parse_alert_creator_nickname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        alert_creator_nickname = _parse_alert_creator_nickname(d.pop("alert_creator_nickname"))

        def _parse_alert_creator_avatar_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        alert_creator_avatar_url = _parse_alert_creator_avatar_url(d.pop("alert_creator_avatar_url"))

        alert_creator_username = d.pop("alert_creator_username")

        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        alert = cls(
            account_id=account_id,
            alert_creator_id=alert_creator_id,
            read_only=read_only,
            alert_creator_nickname=alert_creator_nickname,
            alert_creator_avatar_url=alert_creator_avatar_url,
            alert_creator_username=alert_creator_username,
            created_at=created_at,
            id=id,
        )

        alert.additional_properties = d
        return alert

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
