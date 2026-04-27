from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_tiktok_live_user_info import PartialTikTokLiveUserInfo
    from ..models.tik_tok_live_user_raw import TikTokLiveUserRaw
    from ..models.tik_tok_live_user_user import TikTokLiveUserUser


T = TypeVar("T", bound="TikTokLiveUser")


@_attrs_define
class TikTokLiveUser:
    """
    Attributes:
        raw (TikTokLiveUserRaw):
        unique_id (str):
        room_info (PartialTikTokLiveUserInfo | Unset): Make all properties in T optional
        user (TikTokLiveUserUser | Unset):
    """

    raw: TikTokLiveUserRaw
    unique_id: str
    room_info: PartialTikTokLiveUserInfo | Unset = UNSET
    user: TikTokLiveUserUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        raw = self.raw.to_dict()

        unique_id = self.unique_id

        room_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.room_info, Unset):
            room_info = self.room_info.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "raw": raw,
                "unique_id": unique_id,
            }
        )
        if room_info is not UNSET:
            field_dict["room_info"] = room_info
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_tiktok_live_user_info import PartialTikTokLiveUserInfo
        from ..models.tik_tok_live_user_raw import TikTokLiveUserRaw
        from ..models.tik_tok_live_user_user import TikTokLiveUserUser

        d = dict(src_dict)
        raw = TikTokLiveUserRaw.from_dict(d.pop("raw"))

        unique_id = d.pop("unique_id")

        _room_info = d.pop("room_info", UNSET)
        room_info: PartialTikTokLiveUserInfo | Unset
        if isinstance(_room_info, Unset):
            room_info = UNSET
        else:
            room_info = PartialTikTokLiveUserInfo.from_dict(_room_info)

        _user = d.pop("user", UNSET)
        user: TikTokLiveUserUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = TikTokLiveUserUser.from_dict(_user)

        tik_tok_live_user = cls(
            raw=raw,
            unique_id=unique_id,
            room_info=room_info,
            user=user,
        )

        tik_tok_live_user.additional_properties = d
        return tik_tok_live_user

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
