from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_hashtag_list_response_game_category import WebcastHashtagListResponseGameCategory
    from ..models.webcast_hashtag_list_response_hashtag_simple import WebcastHashtagListResponseHashtagSimple


T = TypeVar("T", bound="WebcastHashtagListResponseGameTag")


@_attrs_define
class WebcastHashtagListResponseGameTag:
    """
    Attributes:
        bundle_id (str):
        full_name (str):
        game_category (list[WebcastHashtagListResponseGameCategory]):
        gar (list[Any]):
        hashtag_id (list[Any]):
        hashtag_list (list[WebcastHashtagListResponseHashtagSimple]):
        id (float):
        is_new_game (bool):
        landscape (float):
        package_name (str):
        short_name (str):
        show_name (str):
    """

    bundle_id: str
    full_name: str
    game_category: list[WebcastHashtagListResponseGameCategory]
    gar: list[Any]
    hashtag_id: list[Any]
    hashtag_list: list[WebcastHashtagListResponseHashtagSimple]
    id: float
    is_new_game: bool
    landscape: float
    package_name: str
    short_name: str
    show_name: str

    def to_dict(self) -> dict[str, Any]:
        bundle_id = self.bundle_id

        full_name = self.full_name

        game_category = []
        for game_category_item_data in self.game_category:
            game_category_item = game_category_item_data.to_dict()
            game_category.append(game_category_item)

        gar = self.gar

        hashtag_id = self.hashtag_id

        hashtag_list = []
        for hashtag_list_item_data in self.hashtag_list:
            hashtag_list_item = hashtag_list_item_data.to_dict()
            hashtag_list.append(hashtag_list_item)

        id = self.id

        is_new_game = self.is_new_game

        landscape = self.landscape

        package_name = self.package_name

        short_name = self.short_name

        show_name = self.show_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bundle_id": bundle_id,
                "full_name": full_name,
                "game_category": game_category,
                "gar": gar,
                "hashtag_id": hashtag_id,
                "hashtag_list": hashtag_list,
                "id": id,
                "is_new_game": is_new_game,
                "landscape": landscape,
                "package_name": package_name,
                "short_name": short_name,
                "show_name": show_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_hashtag_list_response_game_category import WebcastHashtagListResponseGameCategory
        from ..models.webcast_hashtag_list_response_hashtag_simple import WebcastHashtagListResponseHashtagSimple

        d = dict(src_dict)
        bundle_id = d.pop("bundle_id")

        full_name = d.pop("full_name")

        game_category = []
        _game_category = d.pop("game_category")
        for game_category_item_data in _game_category:
            game_category_item = WebcastHashtagListResponseGameCategory.from_dict(game_category_item_data)

            game_category.append(game_category_item)

        gar = cast(list[Any], d.pop("gar"))

        hashtag_id = cast(list[Any], d.pop("hashtag_id"))

        hashtag_list = []
        _hashtag_list = d.pop("hashtag_list")
        for hashtag_list_item_data in _hashtag_list:
            hashtag_list_item = WebcastHashtagListResponseHashtagSimple.from_dict(hashtag_list_item_data)

            hashtag_list.append(hashtag_list_item)

        id = d.pop("id")

        is_new_game = d.pop("is_new_game")

        landscape = d.pop("landscape")

        package_name = d.pop("package_name")

        short_name = d.pop("short_name")

        show_name = d.pop("show_name")

        webcast_hashtag_list_response_game_tag = cls(
            bundle_id=bundle_id,
            full_name=full_name,
            game_category=game_category,
            gar=gar,
            hashtag_id=hashtag_id,
            hashtag_list=hashtag_list,
            id=id,
            is_new_game=is_new_game,
            landscape=landscape,
            package_name=package_name,
            short_name=short_name,
            show_name=show_name,
        )

        return webcast_hashtag_list_response_game_tag
