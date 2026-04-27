from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_target import AlertTarget


T = TypeVar("T", bound="CreateAlertTargetResponse")


@_attrs_define
class CreateAlertTargetResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        target (AlertTarget | Unset):
    """

    code: float
    message: str | Unset = UNSET
    target: AlertTarget | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_target import AlertTarget

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _target = d.pop("target", UNSET)
        target: AlertTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = AlertTarget.from_dict(_target)

        create_alert_target_response = cls(
            code=code,
            message=message,
            target=target,
        )

        return create_alert_target_response
