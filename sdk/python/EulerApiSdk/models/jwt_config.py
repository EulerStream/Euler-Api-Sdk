from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.accounts_table_request_limits import AccountsTableRequestLimits
    from ..models.jwt_config_web_socket_data import JWTConfigWebSocketData


T = TypeVar("T", bound="JWTConfig")


@_attrs_define
class JWTConfig:
    """
    Attributes:
        id (str):
        expires_at (float):
        ttl (float):
        account_id (float):
        api_key_id (float):
        limits (AccountsTableRequestLimits):
        web_socket_data (JWTConfigWebSocketData):
        name (None | str):
    """

    id: str
    expires_at: float
    ttl: float
    account_id: float
    api_key_id: float
    limits: AccountsTableRequestLimits
    web_socket_data: JWTConfigWebSocketData
    name: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        expires_at = self.expires_at

        ttl = self.ttl

        account_id = self.account_id

        api_key_id = self.api_key_id

        limits = self.limits.to_dict()

        web_socket_data = self.web_socket_data.to_dict()

        name: None | str
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "expiresAt": expires_at,
                "ttl": ttl,
                "accountId": account_id,
                "apiKeyId": api_key_id,
                "limits": limits,
                "webSocketData": web_socket_data,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounts_table_request_limits import AccountsTableRequestLimits
        from ..models.jwt_config_web_socket_data import JWTConfigWebSocketData

        d = dict(src_dict)
        id = d.pop("id")

        expires_at = d.pop("expiresAt")

        ttl = d.pop("ttl")

        account_id = d.pop("accountId")

        api_key_id = d.pop("apiKeyId")

        limits = AccountsTableRequestLimits.from_dict(d.pop("limits"))

        web_socket_data = JWTConfigWebSocketData.from_dict(d.pop("webSocketData"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        jwt_config = cls(
            id=id,
            expires_at=expires_at,
            ttl=ttl,
            account_id=account_id,
            api_key_id=api_key_id,
            limits=limits,
            web_socket_data=web_socket_data,
            name=name,
        )

        return jwt_config
