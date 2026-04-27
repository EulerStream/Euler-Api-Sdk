from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.alert_target_status import AlertTargetStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestAlertTargetResponse")


@_attrs_define
class TestAlertTargetResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        status (AlertTargetStatus | Unset):
        status_label (str | Unset):
    """

    code: float
    message: str | Unset = UNSET
    status: AlertTargetStatus | Unset = UNSET
    status_label: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_label = self.status_label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if status_label is not UNSET:
            field_dict["statusLabel"] = status_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _status = d.pop("status", UNSET)
        status: AlertTargetStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AlertTargetStatus(_status)

        status_label = d.pop("statusLabel", UNSET)

        test_alert_target_response = cls(
            code=code,
            message=message,
            status=status,
            status_label=status_label,
        )

        return test_alert_target_response
