from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.record_string_number import RecordStringNumber


T = TypeVar("T", bound="WebcastRoomMutedUsersResponseUserAttr")


@_attrs_define
class WebcastRoomMutedUsersResponseUserAttr:
    """
    Attributes:
        admin_permissions (RecordStringNumber): Construct a type with a set of properties K of type T
        has_voting_function (bool):
        is_admin (bool):
        is_channel_admin (bool):
        is_muted (bool):
        is_super_admin (bool):
        mute_duration (float):
    """

    admin_permissions: RecordStringNumber
    has_voting_function: bool
    is_admin: bool
    is_channel_admin: bool
    is_muted: bool
    is_super_admin: bool
    mute_duration: float

    def to_dict(self) -> dict[str, Any]:
        admin_permissions = self.admin_permissions.to_dict()

        has_voting_function = self.has_voting_function

        is_admin = self.is_admin

        is_channel_admin = self.is_channel_admin

        is_muted = self.is_muted

        is_super_admin = self.is_super_admin

        mute_duration = self.mute_duration

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "admin_permissions": admin_permissions,
                "has_voting_function": has_voting_function,
                "is_admin": is_admin,
                "is_channel_admin": is_channel_admin,
                "is_muted": is_muted,
                "is_super_admin": is_super_admin,
                "mute_duration": mute_duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_number import RecordStringNumber

        d = dict(src_dict)
        admin_permissions = RecordStringNumber.from_dict(d.pop("admin_permissions"))

        has_voting_function = d.pop("has_voting_function")

        is_admin = d.pop("is_admin")

        is_channel_admin = d.pop("is_channel_admin")

        is_muted = d.pop("is_muted")

        is_super_admin = d.pop("is_super_admin")

        mute_duration = d.pop("mute_duration")

        webcast_room_muted_users_response_user_attr = cls(
            admin_permissions=admin_permissions,
            has_voting_function=has_voting_function,
            is_admin=is_admin,
            is_channel_admin=is_channel_admin,
            is_muted=is_muted,
            is_super_admin=is_super_admin,
            mute_duration=mute_duration,
        )

        return webcast_room_muted_users_response_user_attr
