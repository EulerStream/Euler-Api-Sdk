from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="AccountConfig")


@_attrs_define
class AccountConfig:
    """
    Attributes:
        day (float):
        hour (float):
        minute (float):
        name (str):
        webhook_secret (str):
        max_alerts (float):
        max_websockets (float):
        expires_at (datetime.datetime | None):
    """

    day: float
    hour: float
    minute: float
    name: str
    webhook_secret: str
    max_alerts: float
    max_websockets: float
    expires_at: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        hour = self.hour

        minute = self.minute

        name = self.name

        webhook_secret = self.webhook_secret

        max_alerts = self.max_alerts

        max_websockets = self.max_websockets

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "day": day,
                "hour": hour,
                "minute": minute,
                "name": name,
                "webhook_secret": webhook_secret,
                "max_alerts": max_alerts,
                "max_websockets": max_websockets,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day")

        hour = d.pop("hour")

        minute = d.pop("minute")

        name = d.pop("name")

        webhook_secret = d.pop("webhook_secret")

        max_alerts = d.pop("max_alerts")

        max_websockets = d.pop("max_websockets")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        account_config = cls(
            day=day,
            hour=hour,
            minute=minute,
            name=name,
            webhook_secret=webhook_secret,
            max_alerts=max_alerts,
            max_websockets=max_websockets,
            expires_at=expires_at,
        )

        return account_config
