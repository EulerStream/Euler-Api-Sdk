from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.oxy_labs_proxy_region import OxyLabsProxyRegion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webcast_feed_route_output import WebcastFeedRouteOutput


T = TypeVar("T", bound="WebcastFeedRouteResponse")


@_attrs_define
class WebcastFeedRouteResponse:
    """
    Attributes:
        code (float):
        region (OxyLabsProxyRegion):
        message (str | Unset):
        response (WebcastFeedRouteOutput | Unset):
    """

    code: float
    region: OxyLabsProxyRegion
    message: str | Unset = UNSET
    response: WebcastFeedRouteOutput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        region = self.region.value

        message = self.message

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "region": region,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_route_output import WebcastFeedRouteOutput

        d = dict(src_dict)
        code = d.pop("code")

        region = OxyLabsProxyRegion(d.pop("region"))

        message = d.pop("message", UNSET)

        _response = d.pop("response", UNSET)
        response: WebcastFeedRouteOutput | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = WebcastFeedRouteOutput.from_dict(_response)

        webcast_feed_route_response = cls(
            code=code,
            region=region,
            message=message,
            response=response,
        )

        return webcast_feed_route_response
