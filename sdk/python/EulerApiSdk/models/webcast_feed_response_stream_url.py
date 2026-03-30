from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_string_string import RecordStringString
    from ..models.webcast_feed_response_stream_url_flv_pull_url import WebcastFeedResponseStreamUrlFlvPullUrl
    from ..models.webcast_feed_response_stream_url_live_core_sdk_data import WebcastFeedResponseStreamUrlLiveCoreSdkData


T = TypeVar("T", bound="WebcastFeedResponseStreamUrl")


@_attrs_define
class WebcastFeedResponseStreamUrl:
    """
    Attributes:
        rtmp_pull_url (str):
        flv_pull_url (WebcastFeedResponseStreamUrlFlvPullUrl):
        stream_size_width (float):
        stream_size_height (float):
        flv_pull_url_params (RecordStringString | Unset): Construct a type with a set of properties K of type T
        live_core_sdk_data (WebcastFeedResponseStreamUrlLiveCoreSdkData | Unset):
    """

    rtmp_pull_url: str
    flv_pull_url: WebcastFeedResponseStreamUrlFlvPullUrl
    stream_size_width: float
    stream_size_height: float
    flv_pull_url_params: RecordStringString | Unset = UNSET
    live_core_sdk_data: WebcastFeedResponseStreamUrlLiveCoreSdkData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        rtmp_pull_url = self.rtmp_pull_url

        flv_pull_url = self.flv_pull_url.to_dict()

        stream_size_width = self.stream_size_width

        stream_size_height = self.stream_size_height

        flv_pull_url_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flv_pull_url_params, Unset):
            flv_pull_url_params = self.flv_pull_url_params.to_dict()

        live_core_sdk_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_core_sdk_data, Unset):
            live_core_sdk_data = self.live_core_sdk_data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rtmp_pull_url": rtmp_pull_url,
                "flv_pull_url": flv_pull_url,
                "stream_size_width": stream_size_width,
                "stream_size_height": stream_size_height,
            }
        )
        if flv_pull_url_params is not UNSET:
            field_dict["flv_pull_url_params"] = flv_pull_url_params
        if live_core_sdk_data is not UNSET:
            field_dict["live_core_sdk_data"] = live_core_sdk_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_string import RecordStringString
        from ..models.webcast_feed_response_stream_url_flv_pull_url import WebcastFeedResponseStreamUrlFlvPullUrl
        from ..models.webcast_feed_response_stream_url_live_core_sdk_data import (
            WebcastFeedResponseStreamUrlLiveCoreSdkData,
        )

        d = dict(src_dict)
        rtmp_pull_url = d.pop("rtmp_pull_url")

        flv_pull_url = WebcastFeedResponseStreamUrlFlvPullUrl.from_dict(d.pop("flv_pull_url"))

        stream_size_width = d.pop("stream_size_width")

        stream_size_height = d.pop("stream_size_height")

        _flv_pull_url_params = d.pop("flv_pull_url_params", UNSET)
        flv_pull_url_params: RecordStringString | Unset
        if isinstance(_flv_pull_url_params, Unset):
            flv_pull_url_params = UNSET
        else:
            flv_pull_url_params = RecordStringString.from_dict(_flv_pull_url_params)

        _live_core_sdk_data = d.pop("live_core_sdk_data", UNSET)
        live_core_sdk_data: WebcastFeedResponseStreamUrlLiveCoreSdkData | Unset
        if isinstance(_live_core_sdk_data, Unset):
            live_core_sdk_data = UNSET
        else:
            live_core_sdk_data = WebcastFeedResponseStreamUrlLiveCoreSdkData.from_dict(_live_core_sdk_data)

        webcast_feed_response_stream_url = cls(
            rtmp_pull_url=rtmp_pull_url,
            flv_pull_url=flv_pull_url,
            stream_size_width=stream_size_width,
            stream_size_height=stream_size_height,
            flv_pull_url_params=flv_pull_url_params,
            live_core_sdk_data=live_core_sdk_data,
        )

        return webcast_feed_response_stream_url
