from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_traffic_conversion import (
        WebcastLiveAnalyticsVideoDetailResponseTrafficConversion,
    )
    from ..models.webcast_live_analytics_video_detail_response_traffic_total import (
        WebcastLiveAnalyticsVideoDetailResponseTrafficTotal,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseTrafficInfo")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseTrafficInfo:
    """
    Attributes:
        total (WebcastLiveAnalyticsVideoDetailResponseTrafficTotal):
        traffic_conversion (WebcastLiveAnalyticsVideoDetailResponseTrafficConversion):
    """

    total: WebcastLiveAnalyticsVideoDetailResponseTrafficTotal
    traffic_conversion: WebcastLiveAnalyticsVideoDetailResponseTrafficConversion

    def to_dict(self) -> dict[str, Any]:
        total = self.total.to_dict()

        traffic_conversion = self.traffic_conversion.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "traffic_conversion": traffic_conversion,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_traffic_conversion import (
            WebcastLiveAnalyticsVideoDetailResponseTrafficConversion,
        )
        from ..models.webcast_live_analytics_video_detail_response_traffic_total import (
            WebcastLiveAnalyticsVideoDetailResponseTrafficTotal,
        )

        d = dict(src_dict)
        total = WebcastLiveAnalyticsVideoDetailResponseTrafficTotal.from_dict(d.pop("total"))

        traffic_conversion = WebcastLiveAnalyticsVideoDetailResponseTrafficConversion.from_dict(
            d.pop("traffic_conversion")
        )

        webcast_live_analytics_video_detail_response_traffic_info = cls(
            total=total,
            traffic_conversion=traffic_conversion,
        )

        return webcast_live_analytics_video_detail_response_traffic_info
