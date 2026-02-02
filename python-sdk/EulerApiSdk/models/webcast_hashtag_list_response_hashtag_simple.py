from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastHashtagListResponseHashtagSimple")


@_attrs_define
class WebcastHashtagListResponseHashtagSimple:
    """
    Attributes:
        id (float):
        namespace (float):
        title (str):
    """

    id: float
    namespace: float
    title: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        namespace = self.namespace

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "namespace": namespace,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        namespace = d.pop("namespace")

        title = d.pop("title")

        webcast_hashtag_list_response_hashtag_simple = cls(
            id=id,
            namespace=namespace,
            title=title,
        )

        return webcast_hashtag_list_response_hashtag_simple
