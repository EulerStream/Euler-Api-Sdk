from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_error_response import TokenErrorResponse
    from ..models.token_response import TokenResponse


T = TypeVar("T", bound="OAuthTokenResponse")


@_attrs_define
class OAuthTokenResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        data (TokenResponse | Unset):
        error (TokenErrorResponse | Unset):
    """

    code: float
    message: str | Unset = UNSET
    data: TokenResponse | Unset = UNSET
    error: TokenErrorResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_error_response import TokenErrorResponse
        from ..models.token_response import TokenResponse

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: TokenResponse | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TokenResponse.from_dict(_data)

        _error = d.pop("error", UNSET)
        error: TokenErrorResponse | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = TokenErrorResponse.from_dict(_error)

        o_auth_token_response = cls(
            code=code,
            message=message,
            data=data,
            error=error,
        )

        return o_auth_token_response
