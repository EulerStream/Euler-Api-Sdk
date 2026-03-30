from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.o_auth_scope import OAuthScope
from ..models.token_response_token_type import TokenResponseTokenType

T = TypeVar("T", bound="TokenResponse")


@_attrs_define
class TokenResponse:
    """
    Attributes:
        access_token (str):
        refresh_token (str):
        token_type (TokenResponseTokenType):
        expires_in (float): Access token lifetime in seconds
        refresh_expires_in (float): Refresh token lifetime in seconds
        scopes (list[OAuthScope]):
    """

    access_token: str
    refresh_token: str
    token_type: TokenResponseTokenType
    expires_in: float
    refresh_expires_in: float
    scopes: list[OAuthScope]

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        refresh_token = self.refresh_token

        token_type = self.token_type.value

        expires_in = self.expires_in

        refresh_expires_in = self.refresh_expires_in

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": token_type,
                "expires_in": expires_in,
                "refresh_expires_in": refresh_expires_in,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token")

        refresh_token = d.pop("refresh_token")

        token_type = TokenResponseTokenType(d.pop("token_type"))

        expires_in = d.pop("expires_in")

        refresh_expires_in = d.pop("refresh_expires_in")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = OAuthScope(scopes_item_data)

            scopes.append(scopes_item)

        token_response = cls(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type=token_type,
            expires_in=expires_in,
            refresh_expires_in=refresh_expires_in,
            scopes=scopes,
        )

        return token_response
