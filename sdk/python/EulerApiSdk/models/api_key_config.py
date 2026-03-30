from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ApiKeyConfig")


@_attrs_define
class ApiKeyConfig:
    """
    Attributes:
        name (str):
        value (str):
        account_id (float):
    """

    name: str
    value: str
    account_id: float

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        account_id = self.account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "value": value,
                "account_id": account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        account_id = d.pop("account_id")

        api_key_config = cls(
            name=name,
            value=value,
            account_id=account_id,
        )

        return api_key_config
