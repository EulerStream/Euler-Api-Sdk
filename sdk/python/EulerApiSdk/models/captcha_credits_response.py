from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptchaCreditsResponse")


@_attrs_define
class CaptchaCreditsResponse:
    """
    Attributes:
        code (float):
        credits_ (float):
        message (str | Unset):
    """

    code: float
    credits_: float
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        credits_ = self.credits_

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "credits": credits_,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        credits_ = d.pop("credits")

        message = d.pop("message", UNSET)

        captcha_credits_response = cls(
            code=code,
            credits_=credits_,
            message=message,
        )

        return captcha_credits_response
