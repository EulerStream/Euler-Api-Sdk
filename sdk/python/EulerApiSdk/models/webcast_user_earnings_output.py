from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webcast_user_earnings_output_earnings_estimate_currency_type_1 import (
    WebcastUserEarningsOutputEarningsEstimateCurrencyType1,
)
from ..models.webcast_user_earnings_output_earnings_estimate_currency_type_2_type_1 import (
    WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1,
)
from ..models.webcast_user_earnings_output_earnings_estimate_currency_type_3_type_1 import (
    WebcastUserEarningsOutputEarningsEstimateCurrencyType3Type1,
)
from ..models.webcast_user_earnings_output_period import WebcastUserEarningsOutputPeriod

if TYPE_CHECKING:
    from ..models.tik_tok_live_user import TikTokLiveUser


T = TypeVar("T", bound="WebcastUserEarningsOutput")


@_attrs_define
class WebcastUserEarningsOutput:
    """
    Attributes:
        user (TikTokLiveUser):
        earnings_estimate_currency (None | WebcastUserEarningsOutputEarningsEstimateCurrencyType1 |
            WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1 |
            WebcastUserEarningsOutputEarningsEstimateCurrencyType3Type1):
        earnings_estimate (float | None):
        diamonds (float | None):
        period (WebcastUserEarningsOutputPeriod):
        resets_at (datetime.datetime | None):
        resets_in (float | None):
    """

    user: TikTokLiveUser
    earnings_estimate_currency: (
        None
        | WebcastUserEarningsOutputEarningsEstimateCurrencyType1
        | WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1
        | WebcastUserEarningsOutputEarningsEstimateCurrencyType3Type1
    )
    earnings_estimate: float | None
    diamonds: float | None
    period: WebcastUserEarningsOutputPeriod
    resets_at: datetime.datetime | None
    resets_in: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        earnings_estimate_currency: None | str
        if isinstance(self.earnings_estimate_currency, WebcastUserEarningsOutputEarningsEstimateCurrencyType1):
            earnings_estimate_currency = self.earnings_estimate_currency.value
        elif isinstance(self.earnings_estimate_currency, WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1):
            earnings_estimate_currency = self.earnings_estimate_currency.value
        elif isinstance(self.earnings_estimate_currency, WebcastUserEarningsOutputEarningsEstimateCurrencyType3Type1):
            earnings_estimate_currency = self.earnings_estimate_currency.value
        else:
            earnings_estimate_currency = self.earnings_estimate_currency

        earnings_estimate: float | None
        earnings_estimate = self.earnings_estimate

        diamonds: float | None
        diamonds = self.diamonds

        period = self.period.value

        resets_at: None | str
        if isinstance(self.resets_at, datetime.datetime):
            resets_at = self.resets_at.isoformat()
        else:
            resets_at = self.resets_at

        resets_in: float | None
        resets_in = self.resets_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "earnings_estimate_currency": earnings_estimate_currency,
                "earnings_estimate": earnings_estimate,
                "diamonds": diamonds,
                "period": period,
                "resets_at": resets_at,
                "resets_in": resets_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_live_user import TikTokLiveUser

        d = dict(src_dict)
        user = TikTokLiveUser.from_dict(d.pop("user"))

        def _parse_earnings_estimate_currency(
            data: object,
        ) -> (
            None
            | WebcastUserEarningsOutputEarningsEstimateCurrencyType1
            | WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1
            | WebcastUserEarningsOutputEarningsEstimateCurrencyType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                earnings_estimate_currency_type_1 = WebcastUserEarningsOutputEarningsEstimateCurrencyType1(data)

                return earnings_estimate_currency_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                earnings_estimate_currency_type_2_type_1 = WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1(
                    data
                )

                return earnings_estimate_currency_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                earnings_estimate_currency_type_3_type_1 = WebcastUserEarningsOutputEarningsEstimateCurrencyType3Type1(
                    data
                )

                return earnings_estimate_currency_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | WebcastUserEarningsOutputEarningsEstimateCurrencyType1
                | WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1
                | WebcastUserEarningsOutputEarningsEstimateCurrencyType3Type1,
                data,
            )

        earnings_estimate_currency = _parse_earnings_estimate_currency(d.pop("earnings_estimate_currency"))

        def _parse_earnings_estimate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        earnings_estimate = _parse_earnings_estimate(d.pop("earnings_estimate"))

        def _parse_diamonds(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        diamonds = _parse_diamonds(d.pop("diamonds"))

        period = WebcastUserEarningsOutputPeriod(d.pop("period"))

        def _parse_resets_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resets_at_type_0 = isoparse(data)

                return resets_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resets_at = _parse_resets_at(d.pop("resets_at"))

        def _parse_resets_in(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        resets_in = _parse_resets_in(d.pop("resets_in"))

        webcast_user_earnings_output = cls(
            user=user,
            earnings_estimate_currency=earnings_estimate_currency,
            earnings_estimate=earnings_estimate,
            diamonds=diamonds,
            period=period,
            resets_at=resets_at,
            resets_in=resets_in,
        )

        webcast_user_earnings_output.additional_properties = d
        return webcast_user_earnings_output

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
