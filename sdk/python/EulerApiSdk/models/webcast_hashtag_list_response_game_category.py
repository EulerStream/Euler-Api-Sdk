from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastHashtagListResponseGameCategory")


@_attrs_define
class WebcastHashtagListResponseGameCategory:
    """
    Attributes:
        game_type (float):
        title (str):
    """

    game_type: float
    title: str

    def to_dict(self) -> dict[str, Any]:
        game_type = self.game_type

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "game_type": game_type,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        game_type = d.pop("game_type")

        title = d.pop("title")

        webcast_hashtag_list_response_game_category = cls(
            game_type=game_type,
            title=title,
        )

        return webcast_hashtag_list_response_game_category
