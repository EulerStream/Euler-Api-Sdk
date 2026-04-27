from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.revoke_request_body_token_type_hint import RevokeRequestBodyTokenTypeHint
from ..types import UNSET, Unset

T = TypeVar("T", bound="RevokeRequestBody")


@_attrs_define
class RevokeRequestBody:
    """
    Attributes:
        token (str):
        client_id (str):
        client_secret (str):
        token_type_hint (RevokeRequestBodyTokenTypeHint | Unset):
    """

    token: str
    client_id: str
    client_secret: str
    token_type_hint: RevokeRequestBodyTokenTypeHint | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        client_id = self.client_id

        client_secret = self.client_secret

        token_type_hint: str | Unset = UNSET
        if not isinstance(self.token_type_hint, Unset):
            token_type_hint = self.token_type_hint.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "token": token,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )
        if token_type_hint is not UNSET:
            field_dict["token_type_hint"] = token_type_hint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        _token_type_hint = d.pop("token_type_hint", UNSET)
        token_type_hint: RevokeRequestBodyTokenTypeHint | Unset
        if isinstance(_token_type_hint, Unset):
            token_type_hint = UNSET
        else:
            token_type_hint = RevokeRequestBodyTokenTypeHint(_token_type_hint)

        revoke_request_body = cls(
            token=token,
            client_id=client_id,
            client_secret=client_secret,
            token_type_hint=token_type_hint,
        )

        return revoke_request_body
