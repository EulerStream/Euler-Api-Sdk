from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accounts_table_request_limits import AccountsTableRequestLimits
    from ..models.jwt_create_config_web_socket_data import JWTCreateConfigWebSocketData


T = TypeVar("T", bound="JWTCreateConfig")


@_attrs_define
class JWTCreateConfig:
    """
    Attributes:
        expire_after (float):
        limits (AccountsTableRequestLimits | None | Unset):
        websockets (JWTCreateConfigWebSocketData | None | Unset):
        name (str | Unset):
    """

    expire_after: float
    limits: AccountsTableRequestLimits | None | Unset = UNSET
    websockets: JWTCreateConfigWebSocketData | None | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.accounts_table_request_limits import AccountsTableRequestLimits
        from ..models.jwt_create_config_web_socket_data import JWTCreateConfigWebSocketData

        expire_after = self.expire_after

        limits: dict[str, Any] | None | Unset
        if isinstance(self.limits, Unset):
            limits = UNSET
        elif isinstance(self.limits, AccountsTableRequestLimits):
            limits = self.limits.to_dict()
        else:
            limits = self.limits

        websockets: dict[str, Any] | None | Unset
        if isinstance(self.websockets, Unset):
            websockets = UNSET
        elif isinstance(self.websockets, JWTCreateConfigWebSocketData):
            websockets = self.websockets.to_dict()
        else:
            websockets = self.websockets

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expireAfter": expire_after,
            }
        )
        if limits is not UNSET:
            field_dict["limits"] = limits
        if websockets is not UNSET:
            field_dict["websockets"] = websockets
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounts_table_request_limits import AccountsTableRequestLimits
        from ..models.jwt_create_config_web_socket_data import JWTCreateConfigWebSocketData

        d = dict(src_dict)
        expire_after = d.pop("expireAfter")

        def _parse_limits(data: object) -> AccountsTableRequestLimits | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                limits_type_1 = AccountsTableRequestLimits.from_dict(data)

                return limits_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountsTableRequestLimits | None | Unset, data)

        limits = _parse_limits(d.pop("limits", UNSET))

        def _parse_websockets(data: object) -> JWTCreateConfigWebSocketData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                websockets_type_1 = JWTCreateConfigWebSocketData.from_dict(data)

                return websockets_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JWTCreateConfigWebSocketData | None | Unset, data)

        websockets = _parse_websockets(d.pop("websockets", UNSET))

        name = d.pop("name", UNSET)

        jwt_create_config = cls(
            expire_after=expire_after,
            limits=limits,
            websockets=websockets,
            name=name,
        )

        return jwt_create_config
