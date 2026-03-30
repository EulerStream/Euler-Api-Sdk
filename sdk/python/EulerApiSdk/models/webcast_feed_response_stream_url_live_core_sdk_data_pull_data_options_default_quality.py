from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptionsDefaultQuality")


@_attrs_define
class WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptionsDefaultQuality:
    """
    Attributes:
        sdk_key (str):
        name (str):
    """

    sdk_key: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sdk_key = self.sdk_key

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sdk_key": sdk_key,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sdk_key = d.pop("sdk_key")

        name = d.pop("name")

        webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options_default_quality = cls(
            sdk_key=sdk_key,
            name=name,
        )

        webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options_default_quality.additional_properties = d
        return webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options_default_quality

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
