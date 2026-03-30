from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key import ApiKey


T = TypeVar("T", bound="UpdateKeyResponse")


@_attrs_define
class UpdateKeyResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        config (ApiKey | Unset):
    """

    code: float
    message: str | Unset = UNSET
    config: ApiKey | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key import ApiKey

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _config = d.pop("config", UNSET)
        config: ApiKey | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ApiKey.from_dict(_config)

        update_key_response = cls(
            code=code,
            message=message,
            config=config,
        )

        return update_key_response
