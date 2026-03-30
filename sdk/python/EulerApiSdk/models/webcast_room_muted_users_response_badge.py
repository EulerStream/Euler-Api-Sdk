from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webcast_room_muted_users_response_badge_combine import WebcastRoomMutedUsersResponseBadgeCombine
    from ..models.webcast_room_muted_users_response_badge_text import WebcastRoomMutedUsersResponseBadgeText
    from ..models.webcast_room_muted_users_response_privilege_log_extra import (
        WebcastRoomMutedUsersResponsePrivilegeLogExtra,
    )


T = TypeVar("T", bound="WebcastRoomMutedUsersResponseBadge")


@_attrs_define
class WebcastRoomMutedUsersResponseBadge:
    """
    Attributes:
        display (bool):
        display_status (float):
        display_type (float):
        exhibition_type (float):
        greyed_by_client (float):
        is_customized (bool):
        position (float):
        priority_type (float):
        privilege_log_extra (WebcastRoomMutedUsersResponsePrivilegeLogExtra):
        scene_type (float):
        open_web_url (str | Unset):
        combine (WebcastRoomMutedUsersResponseBadgeCombine | Unset):
        text (WebcastRoomMutedUsersResponseBadgeText | Unset):
    """

    display: bool
    display_status: float
    display_type: float
    exhibition_type: float
    greyed_by_client: float
    is_customized: bool
    position: float
    priority_type: float
    privilege_log_extra: WebcastRoomMutedUsersResponsePrivilegeLogExtra
    scene_type: float
    open_web_url: str | Unset = UNSET
    combine: WebcastRoomMutedUsersResponseBadgeCombine | Unset = UNSET
    text: WebcastRoomMutedUsersResponseBadgeText | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        display = self.display

        display_status = self.display_status

        display_type = self.display_type

        exhibition_type = self.exhibition_type

        greyed_by_client = self.greyed_by_client

        is_customized = self.is_customized

        position = self.position

        priority_type = self.priority_type

        privilege_log_extra = self.privilege_log_extra.to_dict()

        scene_type = self.scene_type

        open_web_url = self.open_web_url

        combine: dict[str, Any] | Unset = UNSET
        if not isinstance(self.combine, Unset):
            combine = self.combine.to_dict()

        text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "display": display,
                "display_status": display_status,
                "display_type": display_type,
                "exhibition_type": exhibition_type,
                "greyed_by_client": greyed_by_client,
                "is_customized": is_customized,
                "position": position,
                "priority_type": priority_type,
                "privilege_log_extra": privilege_log_extra,
                "scene_type": scene_type,
            }
        )
        if open_web_url is not UNSET:
            field_dict["OpenWebURL"] = open_web_url
        if combine is not UNSET:
            field_dict["combine"] = combine
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_muted_users_response_badge_combine import WebcastRoomMutedUsersResponseBadgeCombine
        from ..models.webcast_room_muted_users_response_badge_text import WebcastRoomMutedUsersResponseBadgeText
        from ..models.webcast_room_muted_users_response_privilege_log_extra import (
            WebcastRoomMutedUsersResponsePrivilegeLogExtra,
        )

        d = dict(src_dict)
        display = d.pop("display")

        display_status = d.pop("display_status")

        display_type = d.pop("display_type")

        exhibition_type = d.pop("exhibition_type")

        greyed_by_client = d.pop("greyed_by_client")

        is_customized = d.pop("is_customized")

        position = d.pop("position")

        priority_type = d.pop("priority_type")

        privilege_log_extra = WebcastRoomMutedUsersResponsePrivilegeLogExtra.from_dict(d.pop("privilege_log_extra"))

        scene_type = d.pop("scene_type")

        open_web_url = d.pop("OpenWebURL", UNSET)

        _combine = d.pop("combine", UNSET)
        combine: WebcastRoomMutedUsersResponseBadgeCombine | Unset
        if isinstance(_combine, Unset):
            combine = UNSET
        else:
            combine = WebcastRoomMutedUsersResponseBadgeCombine.from_dict(_combine)

        _text = d.pop("text", UNSET)
        text: WebcastRoomMutedUsersResponseBadgeText | Unset
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = WebcastRoomMutedUsersResponseBadgeText.from_dict(_text)

        webcast_room_muted_users_response_badge = cls(
            display=display,
            display_status=display_status,
            display_type=display_type,
            exhibition_type=exhibition_type,
            greyed_by_client=greyed_by_client,
            is_customized=is_customized,
            position=position,
            priority_type=priority_type,
            privilege_log_extra=privilege_log_extra,
            scene_type=scene_type,
            open_web_url=open_web_url,
            combine=combine,
            text=text,
        )

        return webcast_room_muted_users_response_badge
