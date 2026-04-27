from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebcastFeedResponseStreamUrlFlvPullUrl")


@_attrs_define
class WebcastFeedResponseStreamUrlFlvPullUrl:
    """
    Attributes:
        sd1 (str | Unset):
        sd2 (str | Unset):
        hd1 (str | Unset):
    """

    sd1: str | Unset = UNSET
    sd2: str | Unset = UNSET
    hd1: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sd1 = self.sd1

        sd2 = self.sd2

        hd1 = self.hd1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sd1 is not UNSET:
            field_dict["SD1"] = sd1
        if sd2 is not UNSET:
            field_dict["SD2"] = sd2
        if hd1 is not UNSET:
            field_dict["HD1"] = hd1

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sd1 = d.pop("SD1", UNSET)

        sd2 = d.pop("SD2", UNSET)

        hd1 = d.pop("HD1", UNSET)

        webcast_feed_response_stream_url_flv_pull_url = cls(
            sd1=sd1,
            sd2=sd2,
            hd1=hd1,
        )

        webcast_feed_response_stream_url_flv_pull_url.additional_properties = d
        return webcast_feed_response_stream_url_flv_pull_url

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
