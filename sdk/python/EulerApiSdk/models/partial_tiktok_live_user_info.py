from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialTikTokLiveUserInfo")


@_attrs_define
class PartialTikTokLiveUserInfo:
    """Make all properties in T optional

    Attributes:
        status (float | Unset):
        is_live (bool | Unset):
        id (str | Unset):
        cover_url (str | Unset):
        title (str | Unset):
        start_time (float | Unset):
        current_viewers (float | Unset):
        total_viewers (float | Unset):
        hls_pull_url (str | Unset):
        flv_pull_url (str | Unset):
        hls_pull_url_ld (str | Unset):
        flv_pull_url_ld (str | Unset):
    """

    status: float | Unset = UNSET
    is_live: bool | Unset = UNSET
    id: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    title: str | Unset = UNSET
    start_time: float | Unset = UNSET
    current_viewers: float | Unset = UNSET
    total_viewers: float | Unset = UNSET
    hls_pull_url: str | Unset = UNSET
    flv_pull_url: str | Unset = UNSET
    hls_pull_url_ld: str | Unset = UNSET
    flv_pull_url_ld: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        is_live = self.is_live

        id = self.id

        cover_url = self.cover_url

        title = self.title

        start_time = self.start_time

        current_viewers = self.current_viewers

        total_viewers = self.total_viewers

        hls_pull_url = self.hls_pull_url

        flv_pull_url = self.flv_pull_url

        hls_pull_url_ld = self.hls_pull_url_ld

        flv_pull_url_ld = self.flv_pull_url_ld

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if is_live is not UNSET:
            field_dict["is_live"] = is_live
        if id is not UNSET:
            field_dict["id"] = id
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if title is not UNSET:
            field_dict["title"] = title
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if current_viewers is not UNSET:
            field_dict["current_viewers"] = current_viewers
        if total_viewers is not UNSET:
            field_dict["total_viewers"] = total_viewers
        if hls_pull_url is not UNSET:
            field_dict["hls_pull_url"] = hls_pull_url
        if flv_pull_url is not UNSET:
            field_dict["flv_pull_url"] = flv_pull_url
        if hls_pull_url_ld is not UNSET:
            field_dict["hls_pull_url_ld"] = hls_pull_url_ld
        if flv_pull_url_ld is not UNSET:
            field_dict["flv_pull_url_ld"] = flv_pull_url_ld

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        is_live = d.pop("is_live", UNSET)

        id = d.pop("id", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        title = d.pop("title", UNSET)

        start_time = d.pop("start_time", UNSET)

        current_viewers = d.pop("current_viewers", UNSET)

        total_viewers = d.pop("total_viewers", UNSET)

        hls_pull_url = d.pop("hls_pull_url", UNSET)

        flv_pull_url = d.pop("flv_pull_url", UNSET)

        hls_pull_url_ld = d.pop("hls_pull_url_ld", UNSET)

        flv_pull_url_ld = d.pop("flv_pull_url_ld", UNSET)

        partial_tiktok_live_user_info = cls(
            status=status,
            is_live=is_live,
            id=id,
            cover_url=cover_url,
            title=title,
            start_time=start_time,
            current_viewers=current_viewers,
            total_viewers=total_viewers,
            hls_pull_url=hls_pull_url,
            flv_pull_url=flv_pull_url,
            hls_pull_url_ld=hls_pull_url_ld,
            flv_pull_url_ld=flv_pull_url_ld,
        )

        partial_tiktok_live_user_info.additional_properties = d
        return partial_tiktok_live_user_info

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
