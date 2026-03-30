from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.record_string_unknown import RecordStringUnknown
    from ..models.webcast_feed_response_image import WebcastFeedResponseImage
    from ..models.webcast_feed_response_user_follow_info import WebcastFeedResponseUserFollowInfo
    from ..models.webcast_feed_response_user_own_room import WebcastFeedResponseUserOwnRoom


T = TypeVar("T", bound="WebcastFeedResponseUser")


@_attrs_define
class WebcastFeedResponseUser:
    """
    Attributes:
        id (float):
        nickname (str):
        bio_description (str):
        avatar_thumb (WebcastFeedResponseImage):
        avatar_medium (WebcastFeedResponseImage):
        avatar_large (WebcastFeedResponseImage):
        status (float):
        modify_time (float):
        follow_info (WebcastFeedResponseUserFollowInfo):
        pay_grade (RecordStringUnknown): Construct a type with a set of properties K of type T
        user_attr (RecordStringUnknown): Construct a type with a set of properties K of type T
        own_room (WebcastFeedResponseUserOwnRoom):
        display_id (str):
        sec_uid (str):
        id_str (str):
    """

    id: float
    nickname: str
    bio_description: str
    avatar_thumb: WebcastFeedResponseImage
    avatar_medium: WebcastFeedResponseImage
    avatar_large: WebcastFeedResponseImage
    status: float
    modify_time: float
    follow_info: WebcastFeedResponseUserFollowInfo
    pay_grade: RecordStringUnknown
    user_attr: RecordStringUnknown
    own_room: WebcastFeedResponseUserOwnRoom
    display_id: str
    sec_uid: str
    id_str: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        nickname = self.nickname

        bio_description = self.bio_description

        avatar_thumb = self.avatar_thumb.to_dict()

        avatar_medium = self.avatar_medium.to_dict()

        avatar_large = self.avatar_large.to_dict()

        status = self.status

        modify_time = self.modify_time

        follow_info = self.follow_info.to_dict()

        pay_grade = self.pay_grade.to_dict()

        user_attr = self.user_attr.to_dict()

        own_room = self.own_room.to_dict()

        display_id = self.display_id

        sec_uid = self.sec_uid

        id_str = self.id_str

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "nickname": nickname,
                "bio_description": bio_description,
                "avatar_thumb": avatar_thumb,
                "avatar_medium": avatar_medium,
                "avatar_large": avatar_large,
                "status": status,
                "modify_time": modify_time,
                "follow_info": follow_info,
                "pay_grade": pay_grade,
                "user_attr": user_attr,
                "own_room": own_room,
                "display_id": display_id,
                "sec_uid": sec_uid,
                "id_str": id_str,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_unknown import RecordStringUnknown
        from ..models.webcast_feed_response_image import WebcastFeedResponseImage
        from ..models.webcast_feed_response_user_follow_info import WebcastFeedResponseUserFollowInfo
        from ..models.webcast_feed_response_user_own_room import WebcastFeedResponseUserOwnRoom

        d = dict(src_dict)
        id = d.pop("id")

        nickname = d.pop("nickname")

        bio_description = d.pop("bio_description")

        avatar_thumb = WebcastFeedResponseImage.from_dict(d.pop("avatar_thumb"))

        avatar_medium = WebcastFeedResponseImage.from_dict(d.pop("avatar_medium"))

        avatar_large = WebcastFeedResponseImage.from_dict(d.pop("avatar_large"))

        status = d.pop("status")

        modify_time = d.pop("modify_time")

        follow_info = WebcastFeedResponseUserFollowInfo.from_dict(d.pop("follow_info"))

        pay_grade = RecordStringUnknown.from_dict(d.pop("pay_grade"))

        user_attr = RecordStringUnknown.from_dict(d.pop("user_attr"))

        own_room = WebcastFeedResponseUserOwnRoom.from_dict(d.pop("own_room"))

        display_id = d.pop("display_id")

        sec_uid = d.pop("sec_uid")

        id_str = d.pop("id_str")

        webcast_feed_response_user = cls(
            id=id,
            nickname=nickname,
            bio_description=bio_description,
            avatar_thumb=avatar_thumb,
            avatar_medium=avatar_medium,
            avatar_large=avatar_large,
            status=status,
            modify_time=modify_time,
            follow_info=follow_info,
            pay_grade=pay_grade,
            user_attr=user_attr,
            own_room=own_room,
            display_id=display_id,
            sec_uid=sec_uid,
            id_str=id_str,
        )

        return webcast_feed_response_user
