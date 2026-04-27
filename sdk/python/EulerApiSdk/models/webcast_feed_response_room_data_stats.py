from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastFeedResponseRoomDataStats")


@_attrs_define
class WebcastFeedResponseRoomDataStats:
    """
    Attributes:
        comment_count (float):
        enter_count (float):
        total_user (float):
    """

    comment_count: float
    enter_count: float
    total_user: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_count = self.comment_count

        enter_count = self.enter_count

        total_user = self.total_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment_count": comment_count,
                "enter_count": enter_count,
                "total_user": total_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_count = d.pop("comment_count")

        enter_count = d.pop("enter_count")

        total_user = d.pop("total_user")

        webcast_feed_response_room_data_stats = cls(
            comment_count=comment_count,
            enter_count=enter_count,
            total_user=total_user,
        )

        webcast_feed_response_room_data_stats.additional_properties = d
        return webcast_feed_response_room_data_stats

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
