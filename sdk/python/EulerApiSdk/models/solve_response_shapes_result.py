from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.shapes_result import ShapesResult


T = TypeVar("T", bound="SolveResponseShapesResult")


@_attrs_define
class SolveResponseShapesResult:
    """
    Attributes:
        response (None | ShapesResult):
        cached (bool):
        code (float):
    """

    response: None | ShapesResult
    cached: bool
    code: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.shapes_result import ShapesResult

        response: dict[str, Any] | None
        if isinstance(self.response, ShapesResult):
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
        from ..models.shapes_result import ShapesResult

        d = dict(src_dict)

        def _parse_response(data: object) -> None | ShapesResult:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_1 = ShapesResult.from_dict(data)

                return response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ShapesResult, data)

        response = _parse_response(d.pop("response"))

        cached = d.pop("cached")

        code = d.pop("code")

        solve_response_shapes_result = cls(
            response=response,
            cached=cached,
            code=code,
        )

        solve_response_shapes_result.additional_properties = d
        return solve_response_shapes_result

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
