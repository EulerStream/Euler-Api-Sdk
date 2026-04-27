from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key import ApiKey


T = TypeVar("T", bound="ListKeysResponse")


@_attrs_define
class ListKeysResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        keys (list[ApiKey] | Unset):
    """

    code: float
    message: str | Unset = UNSET
    keys: list[ApiKey] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item = keys_item_data.to_dict()
                keys.append(keys_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key import ApiKey

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _keys = d.pop("keys", UNSET)
        keys: list[ApiKey] | Unset = UNSET
        if _keys is not UNSET:
            keys = []
            for keys_item_data in _keys:
                keys_item = ApiKey.from_dict(keys_item_data)

                keys.append(keys_item)

        list_keys_response = cls(
            code=code,
            message=message,
            keys=keys,
        )

        return list_keys_response
