from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key import ApiKey


T = TypeVar("T", bound="RetrieveKeyResponse")


@_attrs_define
class RetrieveKeyResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        key (ApiKey | Unset):
    """

    code: float
    message: str | Unset = UNSET
    key: ApiKey | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key import ApiKey

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _key = d.pop("key", UNSET)
        key: ApiKey | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = ApiKey.from_dict(_key)

        retrieve_key_response = cls(
            code=code,
            message=message,
            key=key,
        )

        return retrieve_key_response
