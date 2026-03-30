from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenErrorResponse")


@_attrs_define
class TokenErrorResponse:
    """
    Attributes:
        error (str):
        error_description (str | Unset):
    """

    error: str
    error_description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        error_description = self.error_description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "error": error,
            }
        )
        if error_description is not UNSET:
            field_dict["error_description"] = error_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        error_description = d.pop("error_description", UNSET)

        token_error_response = cls(
            error=error,
            error_description=error_description,
        )

        return token_error_response
