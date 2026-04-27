from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.alert_target_format import AlertTargetFormat
from ..models.alert_target_status import AlertTargetStatus

if TYPE_CHECKING:
    from ..models.record_string_any import RecordStringAny


T = TypeVar("T", bound="AlertTarget")


@_attrs_define
class AlertTarget:
    """
    Attributes:
        url (str):
        metadata (RecordStringAny): Construct a type with a set of properties K of type T
        alert_id (float):
        alert_creator_id (float):
        last_status (AlertTargetStatus):
        format_ (AlertTargetFormat):
        account_id (float):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        id (float):
    """

    url: str
    metadata: RecordStringAny
    alert_id: float
    alert_creator_id: float
    last_status: AlertTargetStatus
    format_: AlertTargetFormat
    account_id: float
    updated_at: datetime.datetime
    created_at: datetime.datetime
    id: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        metadata = self.metadata.to_dict()

        alert_id = self.alert_id

        alert_creator_id = self.alert_creator_id

        last_status = self.last_status.value

        format_ = self.format_.value

        account_id = self.account_id

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "metadata": metadata,
                "alert_id": alert_id,
                "alert_creator_id": alert_creator_id,
                "last_status": last_status,
                "format": format_,
                "account_id": account_id,
                "updated_at": updated_at,
                "created_at": created_at,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_any import RecordStringAny

        d = dict(src_dict)
        url = d.pop("url")

        metadata = RecordStringAny.from_dict(d.pop("metadata"))

        alert_id = d.pop("alert_id")

        alert_creator_id = d.pop("alert_creator_id")

        last_status = AlertTargetStatus(d.pop("last_status"))

        format_ = AlertTargetFormat(d.pop("format"))

        account_id = d.pop("account_id")

        updated_at = isoparse(d.pop("updated_at"))

        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        alert_target = cls(
            url=url,
            metadata=metadata,
            alert_id=alert_id,
            alert_creator_id=alert_creator_id,
            last_status=last_status,
            format_=format_,
            account_id=account_id,
            updated_at=updated_at,
            created_at=created_at,
            id=id,
        )

        alert_target.additional_properties = d
        return alert_target

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
