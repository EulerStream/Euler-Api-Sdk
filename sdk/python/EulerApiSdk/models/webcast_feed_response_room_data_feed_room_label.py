from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastFeedResponseRoomDataFeedRoomLabel")


@_attrs_define
class WebcastFeedResponseRoomDataFeedRoomLabel:
    """
    Attributes:
        url_list (list[str]):
        uri (str):
        avg_color (str):
    """

    url_list: list[str]
    uri: str
    avg_color: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url_list = self.url_list

        uri = self.uri

        avg_color = self.avg_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url_list": url_list,
                "uri": uri,
                "avg_color": avg_color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url_list = cast(list[str], d.pop("url_list"))

        uri = d.pop("uri")

        avg_color = d.pop("avg_color")

        webcast_feed_response_room_data_feed_room_label = cls(
            url_list=url_list,
            uri=uri,
            avg_color=avg_color,
        )

        webcast_feed_response_room_data_feed_room_label.additional_properties = d
        return webcast_feed_response_room_data_feed_room_label

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
