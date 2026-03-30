from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastFeedResponseImage")


@_attrs_define
class WebcastFeedResponseImage:
    """
    Attributes:
        url_list (list[str]):
        uri (str):
    """

    url_list: list[str]
    uri: str

    def to_dict(self) -> dict[str, Any]:
        url_list = self.url_list

        uri = self.uri

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url_list": url_list,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url_list = cast(list[str], d.pop("url_list"))

        uri = d.pop("uri")

        webcast_feed_response_image = cls(
            url_list=url_list,
            uri=uri,
        )

        return webcast_feed_response_image
