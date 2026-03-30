from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whirl_result import WhirlResult


T = TypeVar("T", bound="WhirlCaptchaResponse")


@_attrs_define
class WhirlCaptchaResponse:
    """
    Attributes:
        response (None | WhirlResult):
        cached (bool):
        code (float):
        message (str | Unset):
    """

    response: None | WhirlResult
    cached: bool
    code: float
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.whirl_result import WhirlResult

        response: dict[str, Any] | None
        if isinstance(self.response, WhirlResult):
            response = self.response.to_dict()
        else:
            response = self.response

        cached = self.cached

        code = self.code

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response": response,
                "cached": cached,
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whirl_result import WhirlResult

        d = dict(src_dict)

        def _parse_response(data: object) -> None | WhirlResult:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_1 = WhirlResult.from_dict(data)

                return response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WhirlResult, data)

        response = _parse_response(d.pop("response"))

        cached = d.pop("cached")

        code = d.pop("code")

        message = d.pop("message", UNSET)

        whirl_captcha_response = cls(
            response=response,
            cached=cached,
            code=code,
            message=message,
        )

        whirl_captcha_response.additional_properties = d
        return whirl_captcha_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
