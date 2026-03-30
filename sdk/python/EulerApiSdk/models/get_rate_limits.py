from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_shed_info import LoadShedInfo
    from ..models.rate_limit_info import RateLimitInfo


T = TypeVar("T", bound="GetRateLimits")


@_attrs_define
class GetRateLimits:
    """
    Attributes:
        code (float):
        load_shedding (LoadShedInfo):
        message (str | Unset):
        day (RateLimitInfo | Unset):
        hour (RateLimitInfo | Unset):
        minute (RateLimitInfo | Unset):
    """

    code: float
    load_shedding: LoadShedInfo
    message: str | Unset = UNSET
    day: RateLimitInfo | Unset = UNSET
    hour: RateLimitInfo | Unset = UNSET
    minute: RateLimitInfo | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        load_shedding = self.load_shedding.to_dict()

        message = self.message

        day: dict[str, Any] | Unset = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.to_dict()

        hour: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hour, Unset):
            hour = self.hour.to_dict()

        minute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minute, Unset):
            minute = self.minute.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "load_shedding": load_shedding,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if day is not UNSET:
            field_dict["day"] = day
        if hour is not UNSET:
            field_dict["hour"] = hour
        if minute is not UNSET:
            field_dict["minute"] = minute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_shed_info import LoadShedInfo
        from ..models.rate_limit_info import RateLimitInfo

        d = dict(src_dict)
        code = d.pop("code")

        load_shedding = LoadShedInfo.from_dict(d.pop("load_shedding"))

        message = d.pop("message", UNSET)

        _day = d.pop("day", UNSET)
        day: RateLimitInfo | Unset
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = RateLimitInfo.from_dict(_day)

        _hour = d.pop("hour", UNSET)
        hour: RateLimitInfo | Unset
        if isinstance(_hour, Unset):
            hour = UNSET
        else:
            hour = RateLimitInfo.from_dict(_hour)

        _minute = d.pop("minute", UNSET)
        minute: RateLimitInfo | Unset
        if isinstance(_minute, Unset):
            minute = UNSET
        else:
            minute = RateLimitInfo.from_dict(_minute)

        get_rate_limits = cls(
            code=code,
            load_shedding=load_shedding,
            message=message,
            day=day,
            hour=hour,
            minute=minute,
        )

        return get_rate_limits
