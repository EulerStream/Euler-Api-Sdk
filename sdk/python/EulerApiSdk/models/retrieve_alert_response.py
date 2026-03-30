from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert
    from ..models.retrieve_alert_response_creator import RetrieveAlertResponseCreator


T = TypeVar("T", bound="RetrieveAlertResponse")


@_attrs_define
class RetrieveAlertResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        alert (Alert | Unset):
        creator (RetrieveAlertResponseCreator | Unset):
    """

    code: float
    message: str | Unset = UNSET
    alert: Alert | Unset = UNSET
    creator: RetrieveAlertResponseCreator | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        alert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

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
        if creator is not UNSET:
            field_dict["creator"] = creator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert import Alert
        from ..models.retrieve_alert_response_creator import RetrieveAlertResponseCreator

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _alert = d.pop("alert", UNSET)
        alert: Alert | Unset
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = Alert.from_dict(_alert)

        _creator = d.pop("creator", UNSET)
        creator: RetrieveAlertResponseCreator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RetrieveAlertResponseCreator.from_dict(_creator)

        retrieve_alert_response = cls(
            code=code,
            message=message,
            alert=alert,
            creator=creator,
        )

        return retrieve_alert_response
