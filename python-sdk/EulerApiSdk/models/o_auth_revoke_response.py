from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_error_response import TokenErrorResponse


T = TypeVar("T", bound="OAuthRevokeResponse")


@_attrs_define
class OAuthRevokeResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        error (TokenErrorResponse | Unset):
    """

    code: float
    message: str | Unset = UNSET
    error: TokenErrorResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

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
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_error_response import TokenErrorResponse

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _error = d.pop("error", UNSET)
        error: TokenErrorResponse | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = TokenErrorResponse.from_dict(_error)

        o_auth_revoke_response = cls(
            code=code,
            message=message,
            error=error,
        )

        return o_auth_revoke_response
