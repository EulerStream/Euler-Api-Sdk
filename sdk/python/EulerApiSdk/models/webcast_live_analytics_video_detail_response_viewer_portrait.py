from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_viewers_age import (
        WebcastLiveAnalyticsVideoDetailResponseViewersAge,
    )
    from ..models.webcast_live_analytics_video_detail_response_viewers_gender import (
        WebcastLiveAnalyticsVideoDetailResponseViewersGender,
    )
    from ..models.webcast_live_analytics_video_detail_response_viewers_region import (
        WebcastLiveAnalyticsVideoDetailResponseViewersRegion,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewerPortrait")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewerPortrait:
    """
    Attributes:
        viewers_age (list[WebcastLiveAnalyticsVideoDetailResponseViewersAge]):
        viewers_gender (WebcastLiveAnalyticsVideoDetailResponseViewersGender):
        viewers_region (WebcastLiveAnalyticsVideoDetailResponseViewersRegion):
    """

    viewers_age: list[WebcastLiveAnalyticsVideoDetailResponseViewersAge]
    viewers_gender: WebcastLiveAnalyticsVideoDetailResponseViewersGender
    viewers_region: WebcastLiveAnalyticsVideoDetailResponseViewersRegion

    def to_dict(self) -> dict[str, Any]:
        viewers_age = []
        for viewers_age_item_data in self.viewers_age:
            viewers_age_item = viewers_age_item_data.to_dict()
            viewers_age.append(viewers_age_item)

        viewers_gender = self.viewers_gender.to_dict()

        viewers_region = self.viewers_region.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "viewers_age": viewers_age,
                "viewers_gender": viewers_gender,
                "viewers_region": viewers_region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_viewers_age import (
            WebcastLiveAnalyticsVideoDetailResponseViewersAge,
        )
        from ..models.webcast_live_analytics_video_detail_response_viewers_gender import (
            WebcastLiveAnalyticsVideoDetailResponseViewersGender,
        )
        from ..models.webcast_live_analytics_video_detail_response_viewers_region import (
            WebcastLiveAnalyticsVideoDetailResponseViewersRegion,
        )

        d = dict(src_dict)
        viewers_age = []
        _viewers_age = d.pop("viewers_age")
        for viewers_age_item_data in _viewers_age:
            viewers_age_item = WebcastLiveAnalyticsVideoDetailResponseViewersAge.from_dict(viewers_age_item_data)

            viewers_age.append(viewers_age_item)

        viewers_gender = WebcastLiveAnalyticsVideoDetailResponseViewersGender.from_dict(d.pop("viewers_gender"))

        viewers_region = WebcastLiveAnalyticsVideoDetailResponseViewersRegion.from_dict(d.pop("viewers_region"))

        webcast_live_analytics_video_detail_response_viewer_portrait = cls(
            viewers_age=viewers_age,
            viewers_gender=viewers_gender,
            viewers_region=viewers_region,
        )

        return webcast_live_analytics_video_detail_response_viewer_portrait
