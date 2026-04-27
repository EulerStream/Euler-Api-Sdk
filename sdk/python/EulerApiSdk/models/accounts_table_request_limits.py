from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AccountsTableRequestLimits")


@_attrs_define
class AccountsTableRequestLimits:
    """
    Attributes:
        day (float):
        hour (float):
        minute (float):
    """

    day: float
    hour: float
    minute: float

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        hour = self.hour

        minute = self.minute

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "day": day,
                "hour": hour,
                "minute": minute,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day")

        hour = d.pop("hour")

        minute = d.pop("minute")

        accounts_table_request_limits = cls(
            day=day,
            hour=hour,
            minute=minute,
        )

        return accounts_table_request_limits
