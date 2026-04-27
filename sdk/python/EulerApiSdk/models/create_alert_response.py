from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="CreateAlertResponse")


@_attrs_define
class CreateAlertResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        alert (Alert | Unset):
    """

    code: float
    message: str | Unset = UNSET
    alert: Alert | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        alert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if alert is not UNSET:
            field_dict["alert"] = alert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert import Alert

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _alert = d.pop("alert", UNSET)
        alert: Alert | Unset
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = Alert.from_dict(_alert)

        create_alert_response = cls(
            code=code,
            message=message,
            alert=alert,
        )

        return create_alert_response
