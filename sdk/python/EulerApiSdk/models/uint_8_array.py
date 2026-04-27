from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Uint8Array")


@_attrs_define
class Uint8Array:
    """A typed array of 8-bit unsigned integer values. The contents are initialized to 0. If the
    requested number of bytes could not be allocated an exception is raised.

    """

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        uint_8_array = cls()

        return uint_8_array
