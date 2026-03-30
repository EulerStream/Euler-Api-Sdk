from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="CompleteWhirlCaptchaBody")


@_attrs_define
class CompleteWhirlCaptchaBody:
    """
    Attributes:
        outer_image (File): The outer image file
        inner_image (File): The inner image file
    """

    outer_image: File
    inner_image: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outer_image = self.outer_image.to_tuple()

        inner_image = self.inner_image.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outerImage": outer_image,
                "innerImage": inner_image,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("outerImage", self.outer_image.to_tuple()))

        files.append(("innerImage", self.inner_image.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        outer_image = File(payload=BytesIO(d.pop("outerImage")))

        inner_image = File(payload=BytesIO(d.pop("innerImage")))

        complete_whirl_captcha_body = cls(
            outer_image=outer_image,
            inner_image=inner_image,
        )

        complete_whirl_captcha_body.additional_properties = d
        return complete_whirl_captcha_body

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
