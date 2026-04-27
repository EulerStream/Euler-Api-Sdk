from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_hashtag_list_response_image import WebcastHashtagListResponseImage


T = TypeVar("T", bound="WebcastHashtagListResponseHashtag")


@_attrs_define
class WebcastHashtagListResponseHashtag:
    """
    Attributes:
        id (float):
        image (WebcastHashtagListResponseImage):
        namespace (float):
        title (str):
    """

    id: float
    image: WebcastHashtagListResponseImage
    namespace: float
    title: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        image = self.image.to_dict()

        namespace = self.namespace

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "image": image,
                "namespace": namespace,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_hashtag_list_response_image import WebcastHashtagListResponseImage

        d = dict(src_dict)
        id = d.pop("id")

        image = WebcastHashtagListResponseImage.from_dict(d.pop("image"))

        namespace = d.pop("namespace")

        title = d.pop("title")

        webcast_hashtag_list_response_hashtag = cls(
            id=id,
            image=image,
            namespace=namespace,
            title=title,
        )

        return webcast_hashtag_list_response_hashtag
