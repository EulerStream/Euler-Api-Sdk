from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastHashtagListResponseImage")


@_attrs_define
class WebcastHashtagListResponseImage:
    """
    Attributes:
        avg_color (str):
        height (float):
        image_type (float):
        is_animated (bool):
        open_web_url (str):
        uri (str):
        url_list (list[str]):
        width (float):
    """

    avg_color: str
    height: float
    image_type: float
    is_animated: bool
    open_web_url: str
    uri: str
    url_list: list[str]
    width: float

    def to_dict(self) -> dict[str, Any]:
        avg_color = self.avg_color

        height = self.height

        image_type = self.image_type

        is_animated = self.is_animated

        open_web_url = self.open_web_url

        uri = self.uri

        url_list = self.url_list

        width = self.width

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avg_color": avg_color,
                "height": height,
                "image_type": image_type,
                "is_animated": is_animated,
                "open_web_url": open_web_url,
                "uri": uri,
                "url_list": url_list,
                "width": width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_color = d.pop("avg_color")

        height = d.pop("height")

        image_type = d.pop("image_type")

        is_animated = d.pop("is_animated")

        open_web_url = d.pop("open_web_url")

        uri = d.pop("uri")

        url_list = cast(list[str], d.pop("url_list"))

        width = d.pop("width")

        webcast_hashtag_list_response_image = cls(
            avg_color=avg_color,
            height=height,
            image_type=image_type,
            is_animated=is_animated,
            open_web_url=open_web_url,
            uri=uri,
            url_list=url_list,
            width=width,
        )

        return webcast_hashtag_list_response_image
