from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_feed_response_hashtag_image import WebcastFeedResponseHashtagImage


T = TypeVar("T", bound="WebcastFeedResponseHashtag")


@_attrs_define
class WebcastFeedResponseHashtag:
    """
    Attributes:
        id (float):
        title (str):
        image (WebcastFeedResponseHashtagImage):
    """

    id: float
    title: str
    image: WebcastFeedResponseHashtagImage

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        image = self.image.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "title": title,
                "image": image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_hashtag_image import WebcastFeedResponseHashtagImage

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        image = WebcastFeedResponseHashtagImage.from_dict(d.pop("image"))

        webcast_feed_response_hashtag = cls(
            id=id,
            title=title,
            image=image,
        )

        return webcast_feed_response_hashtag
