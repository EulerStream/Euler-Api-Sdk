from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="RetrieveBulkLiveCheckPayload")


@_attrs_define
class RetrieveBulkLiveCheckPayload:
    """
    Attributes:
        user_numeric_ids (list[str]):
    """

    user_numeric_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        user_numeric_ids = self.user_numeric_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "user_numeric_ids": user_numeric_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_numeric_ids = cast(list[str], d.pop("user_numeric_ids"))

        retrieve_bulk_live_check_payload = cls(
            user_numeric_ids=user_numeric_ids,
        )

        return retrieve_bulk_live_check_payload
