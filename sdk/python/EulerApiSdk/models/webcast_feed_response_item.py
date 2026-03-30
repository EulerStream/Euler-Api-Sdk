from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.record_string_unknown import RecordStringUnknown
    from ..models.webcast_feed_response_room_data import WebcastFeedResponseRoomData


T = TypeVar("T", bound="WebcastFeedResponseItem")


@_attrs_define
class WebcastFeedResponseItem:
    """
    Attributes:
        type_ (float):
        rid (str):
        data (WebcastFeedResponseRoomData):
        flare_info (RecordStringUnknown): Construct a type with a set of properties K of type T
        room_event_tracking (str):
    """

    type_: float
    rid: str
    data: WebcastFeedResponseRoomData
    flare_info: RecordStringUnknown
    room_event_tracking: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        rid = self.rid

        data = self.data.to_dict()

        flare_info = self.flare_info.to_dict()

        room_event_tracking = self.room_event_tracking

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "rid": rid,
                "data": data,
                "flare_info": flare_info,
                "room_event_tracking": room_event_tracking,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_unknown import RecordStringUnknown
        from ..models.webcast_feed_response_room_data import WebcastFeedResponseRoomData

        d = dict(src_dict)
        type_ = d.pop("type")

        rid = d.pop("rid")

        data = WebcastFeedResponseRoomData.from_dict(d.pop("data"))

        flare_info = RecordStringUnknown.from_dict(d.pop("flare_info"))

        room_event_tracking = d.pop("room_event_tracking")

        webcast_feed_response_item = cls(
            type_=type_,
            rid=rid,
            data=data,
            flare_info=flare_info,
            room_event_tracking=room_event_tracking,
        )

        return webcast_feed_response_item
