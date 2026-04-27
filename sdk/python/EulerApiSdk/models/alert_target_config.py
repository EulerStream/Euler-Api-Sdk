from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.alert_target_format import AlertTargetFormat
from ..models.alert_target_status import AlertTargetStatus

if TYPE_CHECKING:
    from ..models.record_string_any import RecordStringAny


T = TypeVar("T", bound="AlertTargetConfig")


@_attrs_define
class AlertTargetConfig:
    """
    Attributes:
        url (str):
        metadata (RecordStringAny): Construct a type with a set of properties K of type T
        alert_id (float):
        alert_creator_id (float):
        last_status (AlertTargetStatus):
        format_ (AlertTargetFormat):
    """

    url: str
    metadata: RecordStringAny
    alert_id: float
    alert_creator_id: float
    last_status: AlertTargetStatus
    format_: AlertTargetFormat

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        metadata = self.metadata.to_dict()

        alert_id = self.alert_id

        alert_creator_id = self.alert_creator_id

        last_status = self.last_status.value

        format_ = self.format_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "metadata": metadata,
                "alert_id": alert_id,
                "alert_creator_id": alert_creator_id,
                "last_status": last_status,
                "format": format_,
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

        alert_target_config = cls(
            url=url,
            metadata=metadata,
            alert_id=alert_id,
            alert_creator_id=alert_creator_id,
            last_status=last_status,
            format_=format_,
        )

        return alert_target_config
