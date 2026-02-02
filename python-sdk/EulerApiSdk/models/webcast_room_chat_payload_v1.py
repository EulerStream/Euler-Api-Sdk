from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebcastRoomChatPayloadV1")


@_attrs_define
class WebcastRoomChatPayloadV1:
    """
    Attributes:
        content (str): The chat message content to send
        session_id (str):
        target_room_id (str | Unset): The room ID to send the chat to (either this or targetUniqueId is required)
        target_unique_id (str | Unset): The username of the room to send the chat to (either this or targetRoomId is
            required)
        tt_target_idc (str | Unset):
    """

    content: str
    session_id: str
    target_room_id: str | Unset = UNSET
    target_unique_id: str | Unset = UNSET
    tt_target_idc: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        session_id = self.session_id

        target_room_id = self.target_room_id

        target_unique_id = self.target_unique_id

        tt_target_idc = self.tt_target_idc

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content": content,
                "sessionId": session_id,
            }
        )
        if target_room_id is not UNSET:
            field_dict["targetRoomId"] = target_room_id
        if target_unique_id is not UNSET:
            field_dict["targetUniqueId"] = target_unique_id
        if tt_target_idc is not UNSET:
            field_dict["ttTargetIdc"] = tt_target_idc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        session_id = d.pop("sessionId")

        target_room_id = d.pop("targetRoomId", UNSET)

        target_unique_id = d.pop("targetUniqueId", UNSET)

        tt_target_idc = d.pop("ttTargetIdc", UNSET)

        webcast_room_chat_payload_v1 = cls(
            content=content,
            session_id=session_id,
            target_room_id=target_room_id,
            target_unique_id=target_unique_id,
            tt_target_idc=tt_target_idc,
        )

        return webcast_room_chat_payload_v1
