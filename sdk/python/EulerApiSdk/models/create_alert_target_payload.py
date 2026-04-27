from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_string_any import RecordStringAny


T = TypeVar("T", bound="CreateAlertTargetPayload")


@_attrs_define
class CreateAlertTargetPayload:
    """
    Attributes:
        url (str):
        metadata (RecordStringAny | Unset): Construct a type with a set of properties K of type T
    """

    url: str
    metadata: RecordStringAny | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_any import RecordStringAny

        d = dict(src_dict)
        url = d.pop("url")

        _metadata = d.pop("metadata", UNSET)
        metadata: RecordStringAny | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RecordStringAny.from_dict(_metadata)

        create_alert_target_payload = cls(
            url=url,
            metadata=metadata,
        )

        return create_alert_target_payload
