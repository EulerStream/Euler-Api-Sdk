from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AlertConfig")


@_attrs_define
class AlertConfig:
    """
    Attributes:
        account_id (float):
        alert_creator_id (float):
        read_only (bool):
    """

    account_id: float
    alert_creator_id: float
    read_only: bool

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        alert_creator_id = self.alert_creator_id

        read_only = self.read_only

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account_id": account_id,
                "alert_creator_id": alert_creator_id,
                "read_only": read_only,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        alert_creator_id = d.pop("alert_creator_id")

        read_only = d.pop("read_only")

        alert_config = cls(
            account_id=account_id,
            alert_creator_id=alert_creator_id,
            read_only=read_only,
        )

        return alert_config
