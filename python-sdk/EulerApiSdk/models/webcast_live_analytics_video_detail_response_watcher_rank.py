from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.record_string_unknown import RecordStringUnknown


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseWatcherRank")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseWatcherRank:
    """
    Attributes:
        user (RecordStringUnknown): Construct a type with a set of properties K of type T
        value (float):
    """

    user: RecordStringUnknown
    value: float

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "user": user,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_unknown import RecordStringUnknown

        d = dict(src_dict)
        user = RecordStringUnknown.from_dict(d.pop("user"))

        value = d.pop("value")

        webcast_live_analytics_video_detail_response_watcher_rank = cls(
            user=user,
            value=value,
        )

        return webcast_live_analytics_video_detail_response_watcher_rank
