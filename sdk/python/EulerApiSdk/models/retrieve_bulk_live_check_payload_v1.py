from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrieveBulkLiveCheckPayloadV1")


@_attrs_define
class RetrieveBulkLiveCheckPayloadV1:
    """
    Attributes:
        user_numeric_ids (list[str]):
        session_id (str):
        tt_target_idc (str | Unset):
    """

    user_numeric_ids: list[str]
    session_id: str
    tt_target_idc: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_numeric_ids = self.user_numeric_ids

        session_id = self.session_id

        tt_target_idc = self.tt_target_idc

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "user_numeric_ids": user_numeric_ids,
                "session_id": session_id,
            }
        )
        if tt_target_idc is not UNSET:
            field_dict["tt_target_idc"] = tt_target_idc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_numeric_ids = cast(list[str], d.pop("user_numeric_ids"))

        session_id = d.pop("session_id")

        tt_target_idc = d.pop("tt_target_idc", UNSET)

        retrieve_bulk_live_check_payload_v1 = cls(
            user_numeric_ids=user_numeric_ids,
            session_id=session_id,
            tt_target_idc=tt_target_idc,
        )

        return retrieve_bulk_live_check_payload_v1
