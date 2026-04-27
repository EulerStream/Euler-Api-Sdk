from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tik_tok_live_user import TikTokLiveUser


T = TypeVar("T", bound="WebcastRoomInfoRouteResponse")


@_attrs_define
class WebcastRoomInfoRouteResponse:
    """
    Attributes:
        code (float):
        ok (bool):
        routes_attempted (list[str]):
        data (None | TikTokLiveUser):
        message (str | Unset):
    """

    code: float
    ok: bool
    routes_attempted: list[str]
    data: None | TikTokLiveUser
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.tik_tok_live_user import TikTokLiveUser

        code = self.code

        ok = self.ok

        routes_attempted = self.routes_attempted

        data: dict[str, Any] | None
        if isinstance(self.data, TikTokLiveUser):
            data = self.data.to_dict()
        else:
            data = self.data

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "ok": ok,
                "routes_attempted": routes_attempted,
                "data": data,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_live_user import TikTokLiveUser

        d = dict(src_dict)
        code = d.pop("code")

        ok = d.pop("ok")

        routes_attempted = cast(list[str], d.pop("routes_attempted"))

        def _parse_data(data: object) -> None | TikTokLiveUser:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = TikTokLiveUser.from_dict(data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TikTokLiveUser, data)

        data = _parse_data(d.pop("data"))

        message = d.pop("message", UNSET)

        webcast_room_info_route_response = cls(
            code=code,
            ok=ok,
            routes_attempted=routes_attempted,
            data=data,
            message=message,
        )

        return webcast_room_info_route_response
