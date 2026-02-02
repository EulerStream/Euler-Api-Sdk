from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_room_muted_users_response_image import WebcastRoomMutedUsersResponseImage


T = TypeVar("T", bound="WebcastRoomMutedUsersResponseBadgeBackground")


@_attrs_define
class WebcastRoomMutedUsersResponseBadgeBackground:
    """
    Attributes:
        background_color_code (str):
        border_color_code (str):
        image (WebcastRoomMutedUsersResponseImage):
        left_side_image (WebcastRoomMutedUsersResponseImage):
    """

    background_color_code: str
    border_color_code: str
    image: WebcastRoomMutedUsersResponseImage
    left_side_image: WebcastRoomMutedUsersResponseImage

    def to_dict(self) -> dict[str, Any]:
        background_color_code = self.background_color_code

        border_color_code = self.border_color_code

        image = self.image.to_dict()

        left_side_image = self.left_side_image.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "background_color_code": background_color_code,
                "border_color_code": border_color_code,
                "image": image,
                "left_side_image": left_side_image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_muted_users_response_image import WebcastRoomMutedUsersResponseImage

        d = dict(src_dict)
        background_color_code = d.pop("background_color_code")

        border_color_code = d.pop("border_color_code")

        image = WebcastRoomMutedUsersResponseImage.from_dict(d.pop("image"))

        left_side_image = WebcastRoomMutedUsersResponseImage.from_dict(d.pop("left_side_image"))

        webcast_room_muted_users_response_badge_background = cls(
            background_color_code=background_color_code,
            border_color_code=border_color_code,
            image=image,
            left_side_image=left_side_image,
        )

        return webcast_room_muted_users_response_badge_background
