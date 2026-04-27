from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastFeedResponseRoomDataGameTagDetail")


@_attrs_define
class WebcastFeedResponseRoomDataGameTagDetail:
    """
    Attributes:
        display_name (str):
        starling_key (str):
        game_tag_name (str):
        game_tag_id (float):
    """

    display_name: str
    starling_key: str
    game_tag_name: str
    game_tag_id: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        starling_key = self.starling_key

        game_tag_name = self.game_tag_name

        game_tag_id = self.game_tag_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
                "starling_key": starling_key,
                "game_tag_name": game_tag_name,
                "game_tag_id": game_tag_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        starling_key = d.pop("starling_key")

        game_tag_name = d.pop("game_tag_name")

        game_tag_id = d.pop("game_tag_id")

        webcast_feed_response_room_data_game_tag_detail = cls(
            display_name=display_name,
            starling_key=starling_key,
            game_tag_name=game_tag_name,
            game_tag_id=game_tag_id,
        )

        webcast_feed_response_room_data_game_tag_detail.additional_properties = d
        return webcast_feed_response_room_data_game_tag_detail

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
