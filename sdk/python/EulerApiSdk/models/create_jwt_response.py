from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jwt_config import JWTConfig


T = TypeVar("T", bound="CreateJWTResponse")


@_attrs_define
class CreateJWTResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        token (str | Unset):
        config (JWTConfig | Unset):
    """

    code: float
    message: str | Unset = UNSET
    token: str | Unset = UNSET
    config: JWTConfig | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        token = self.token

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
        if token is not UNSET:
            field_dict["token"] = token
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jwt_config import JWTConfig

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        token = d.pop("token", UNSET)

        _config = d.pop("config", UNSET)
        config: JWTConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = JWTConfig.from_dict(_config)

        create_jwt_response = cls(
            code=code,
            message=message,
            token=token,
            config=config,
        )

        return create_jwt_response
