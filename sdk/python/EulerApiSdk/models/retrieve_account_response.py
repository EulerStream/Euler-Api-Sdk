from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_with_permissions_safe import AccountWithPermissionsSafe


T = TypeVar("T", bound="RetrieveAccountResponse")


@_attrs_define
class RetrieveAccountResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        account (AccountWithPermissionsSafe | Unset):
    """

    code: float
    message: str | Unset = UNSET
    account: AccountWithPermissionsSafe | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if account is not UNSET:
            field_dict["account"] = account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_with_permissions_safe import AccountWithPermissionsSafe

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _account = d.pop("account", UNSET)
        account: AccountWithPermissionsSafe | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = AccountWithPermissionsSafe.from_dict(_account)

        retrieve_account_response = cls(
            code=code,
            message=message,
            account=account,
        )

        return retrieve_account_response
