from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="ListAlertsResponse")


@_attrs_define
class ListAlertsResponse:
    """
    Attributes:
        code (float):
        has_more (bool):
        message (str | Unset):
        alerts (list[Alert] | Unset):
    """

    code: float
    has_more: bool
    message: str | Unset = UNSET
    alerts: list[Alert] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        has_more = self.has_more

        message = self.message

        alerts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item = alerts_item_data.to_dict()
                alerts.append(alerts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "hasMore": has_more,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if alerts is not UNSET:
            field_dict["alerts"] = alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert import Alert

        d = dict(src_dict)
        code = d.pop("code")

        has_more = d.pop("hasMore")

        message = d.pop("message", UNSET)

        _alerts = d.pop("alerts", UNSET)
        alerts: list[Alert] | Unset = UNSET
        if _alerts is not UNSET:
            alerts = []
            for alerts_item_data in _alerts:
                alerts_item = Alert.from_dict(alerts_item_data)

                alerts.append(alerts_item)

        list_alerts_response = cls(
            code=code,
            has_more=has_more,
            message=message,
            alerts=alerts,
        )

        return list_alerts_response
