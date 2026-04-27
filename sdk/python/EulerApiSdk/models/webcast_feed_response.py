from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_feed_response_extra import WebcastFeedResponseExtra
    from ..models.webcast_feed_response_item import WebcastFeedResponseItem


T = TypeVar("T", bound="WebcastFeedResponse")


@_attrs_define
class WebcastFeedResponse:
    """
    Attributes:
        status_code (float):
        extra (WebcastFeedResponseExtra):
        data (list[WebcastFeedResponseItem]):
    """

    status_code: float
    extra: WebcastFeedResponseExtra
    data: list[WebcastFeedResponseItem]

    def to_dict(self) -> dict[str, Any]:
        status_code = self.status_code

        extra = self.extra.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status_code": status_code,
                "extra": extra,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_extra import WebcastFeedResponseExtra
        from ..models.webcast_feed_response_item import WebcastFeedResponseItem

        d = dict(src_dict)
        status_code = d.pop("status_code")

        extra = WebcastFeedResponseExtra.from_dict(d.pop("extra"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = WebcastFeedResponseItem.from_dict(data_item_data)

            data.append(data_item)

        webcast_feed_response = cls(
            status_code=status_code,
            extra=extra,
            data=data,
        )

        return webcast_feed_response
