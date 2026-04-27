from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.icons_result import IconsResult


T = TypeVar("T", bound="SolveResponseIconsResult")


@_attrs_define
class SolveResponseIconsResult:
    """
    Attributes:
        response (IconsResult | None):
        cached (bool):
        code (float):
    """

    response: IconsResult | None
    cached: bool
    code: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.icons_result import IconsResult

        response: dict[str, Any] | None
        if isinstance(self.response, IconsResult):
            response = self.response.to_dict()
        else:
            response = self.response

        cached = self.cached

        code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response": response,
                "cached": cached,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.icons_result import IconsResult

        d = dict(src_dict)

        def _parse_response(data: object) -> IconsResult | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_1 = IconsResult.from_dict(data)

                return response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IconsResult | None, data)

        response = _parse_response(d.pop("response"))

        cached = d.pop("cached")

        code = d.pop("code")

        solve_response_icons_result = cls(
            response=response,
            cached=cached,
            code=code,
        )

        solve_response_icons_result.additional_properties = d
        return solve_response_icons_result

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
