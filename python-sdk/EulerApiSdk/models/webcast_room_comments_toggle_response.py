from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.record_string_unknown import RecordStringUnknown
    from ..models.webcast_room_comments_toggle_response_extra import WebcastRoomCommentsToggleResponseExtra


T = TypeVar("T", bound="WebcastRoomCommentsToggleResponse")


@_attrs_define
class WebcastRoomCommentsToggleResponse:
    """
    Attributes:
        data (RecordStringUnknown): Construct a type with a set of properties K of type T
        extra (WebcastRoomCommentsToggleResponseExtra):
        status_code (float):
    """

    data: RecordStringUnknown
    extra: WebcastRoomCommentsToggleResponseExtra
    status_code: float

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        extra = self.extra.to_dict()

        status_code = self.status_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "extra": extra,
                "status_code": status_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_unknown import RecordStringUnknown
        from ..models.webcast_room_comments_toggle_response_extra import WebcastRoomCommentsToggleResponseExtra

        d = dict(src_dict)
        data = RecordStringUnknown.from_dict(d.pop("data"))

        extra = WebcastRoomCommentsToggleResponseExtra.from_dict(d.pop("extra"))

        status_code = d.pop("status_code")

        webcast_room_comments_toggle_response = cls(
            data=data,
            extra=extra,
            status_code=status_code,
        )

        return webcast_room_comments_toggle_response
