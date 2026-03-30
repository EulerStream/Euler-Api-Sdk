from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_room_muted_users_response_badge_background import WebcastRoomMutedUsersResponseBadgeBackground
    from ..models.webcast_room_muted_users_response_badge_text import WebcastRoomMutedUsersResponseBadgeText
    from ..models.webcast_room_muted_users_response_image import WebcastRoomMutedUsersResponseImage


T = TypeVar("T", bound="WebcastRoomMutedUsersResponseBadgeCombine")


@_attrs_define
class WebcastRoomMutedUsersResponseBadgeCombine:
    """
    Attributes:
        background (WebcastRoomMutedUsersResponseBadgeBackground):
        background_auto_mirrored (bool):
        background_dark_mode (WebcastRoomMutedUsersResponseBadgeBackground):
        display_type (float):
        icon (WebcastRoomMutedUsersResponseImage):
        icon_auto_mirrored (bool):
        multi_guest_show_style (float):
        personal_card_show_style (float):
        public_screen_show_style (float):
        ranklist_online_audience_show_style (float):
        str_ (str):
        text (WebcastRoomMutedUsersResponseBadgeText):
    """

    background: WebcastRoomMutedUsersResponseBadgeBackground
    background_auto_mirrored: bool
    background_dark_mode: WebcastRoomMutedUsersResponseBadgeBackground
    display_type: float
    icon: WebcastRoomMutedUsersResponseImage
    icon_auto_mirrored: bool
    multi_guest_show_style: float
    personal_card_show_style: float
    public_screen_show_style: float
    ranklist_online_audience_show_style: float
    str_: str
    text: WebcastRoomMutedUsersResponseBadgeText

    def to_dict(self) -> dict[str, Any]:
        background = self.background.to_dict()

        background_auto_mirrored = self.background_auto_mirrored

        background_dark_mode = self.background_dark_mode.to_dict()

        display_type = self.display_type

        icon = self.icon.to_dict()

        icon_auto_mirrored = self.icon_auto_mirrored

        multi_guest_show_style = self.multi_guest_show_style

        personal_card_show_style = self.personal_card_show_style

        public_screen_show_style = self.public_screen_show_style

        ranklist_online_audience_show_style = self.ranklist_online_audience_show_style

        str_ = self.str_

        text = self.text.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "background": background,
                "background_auto_mirrored": background_auto_mirrored,
                "background_dark_mode": background_dark_mode,
                "display_type": display_type,
                "icon": icon,
                "icon_auto_mirrored": icon_auto_mirrored,
                "multi_guest_show_style": multi_guest_show_style,
                "personal_card_show_style": personal_card_show_style,
                "public_screen_show_style": public_screen_show_style,
                "ranklist_online_audience_show_style": ranklist_online_audience_show_style,
                "str": str_,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_muted_users_response_badge_background import (
            WebcastRoomMutedUsersResponseBadgeBackground,
        )
        from ..models.webcast_room_muted_users_response_badge_text import WebcastRoomMutedUsersResponseBadgeText
        from ..models.webcast_room_muted_users_response_image import WebcastRoomMutedUsersResponseImage

        d = dict(src_dict)
        background = WebcastRoomMutedUsersResponseBadgeBackground.from_dict(d.pop("background"))

        background_auto_mirrored = d.pop("background_auto_mirrored")

        background_dark_mode = WebcastRoomMutedUsersResponseBadgeBackground.from_dict(d.pop("background_dark_mode"))

        display_type = d.pop("display_type")

        icon = WebcastRoomMutedUsersResponseImage.from_dict(d.pop("icon"))

        icon_auto_mirrored = d.pop("icon_auto_mirrored")

        multi_guest_show_style = d.pop("multi_guest_show_style")

        personal_card_show_style = d.pop("personal_card_show_style")

        public_screen_show_style = d.pop("public_screen_show_style")

        ranklist_online_audience_show_style = d.pop("ranklist_online_audience_show_style")

        str_ = d.pop("str")

        text = WebcastRoomMutedUsersResponseBadgeText.from_dict(d.pop("text"))

        webcast_room_muted_users_response_badge_combine = cls(
            background=background,
            background_auto_mirrored=background_auto_mirrored,
            background_dark_mode=background_dark_mode,
            display_type=display_type,
            icon=icon,
            icon_auto_mirrored=icon_auto_mirrored,
            multi_guest_show_style=multi_guest_show_style,
            personal_card_show_style=personal_card_show_style,
            public_screen_show_style=public_screen_show_style,
            ranklist_online_audience_show_style=ranklist_online_audience_show_style,
            str_=str_,
            text=text,
        )

        return webcast_room_muted_users_response_badge_combine
