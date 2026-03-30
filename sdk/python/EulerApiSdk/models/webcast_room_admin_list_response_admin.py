from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.record_string_number import RecordStringNumber
    from ..models.webcast_room_admin_list_response_image import WebcastRoomAdminListResponseImage


T = TypeVar("T", bound="WebcastRoomAdminListResponseAdmin")


@_attrs_define
class WebcastRoomAdminListResponseAdmin:
    """
    Attributes:
        admin_permissions (RecordStringNumber): Construct a type with a set of properties K of type T
        avatar_large (WebcastRoomAdminListResponseImage):
        avatar_thumb (WebcastRoomAdminListResponseImage):
        display_id (str):
        id (float):
        id_str (str):
        nickname (str):
        sec_uid (str):
    """

    admin_permissions: RecordStringNumber
    avatar_large: WebcastRoomAdminListResponseImage
    avatar_thumb: WebcastRoomAdminListResponseImage
    display_id: str
    id: float
    id_str: str
    nickname: str
    sec_uid: str

    def to_dict(self) -> dict[str, Any]:
        admin_permissions = self.admin_permissions.to_dict()

        avatar_large = self.avatar_large.to_dict()

        avatar_thumb = self.avatar_thumb.to_dict()

        display_id = self.display_id

        id = self.id

        id_str = self.id_str

        nickname = self.nickname

        sec_uid = self.sec_uid

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "admin_permissions": admin_permissions,
                "avatar_large": avatar_large,
                "avatar_thumb": avatar_thumb,
                "display_id": display_id,
                "id": id,
                "id_str": id_str,
                "nickname": nickname,
                "sec_uid": sec_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_number import RecordStringNumber
        from ..models.webcast_room_admin_list_response_image import WebcastRoomAdminListResponseImage

        d = dict(src_dict)
        admin_permissions = RecordStringNumber.from_dict(d.pop("admin_permissions"))

        avatar_large = WebcastRoomAdminListResponseImage.from_dict(d.pop("avatar_large"))

        avatar_thumb = WebcastRoomAdminListResponseImage.from_dict(d.pop("avatar_thumb"))

        display_id = d.pop("display_id")

        id = d.pop("id")

        id_str = d.pop("id_str")

        nickname = d.pop("nickname")

        sec_uid = d.pop("sec_uid")

        webcast_room_admin_list_response_admin = cls(
            admin_permissions=admin_permissions,
            avatar_large=avatar_large,
            avatar_thumb=avatar_thumb,
            display_id=display_id,
            id=id,
            id_str=id_str,
            nickname=nickname,
            sec_uid=sec_uid,
        )

        return webcast_room_admin_list_response_admin
