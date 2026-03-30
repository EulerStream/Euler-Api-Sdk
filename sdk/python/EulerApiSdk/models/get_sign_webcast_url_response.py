from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSignWebcastUrlResponse")


@_attrs_define
class GetSignWebcastUrlResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        signed_url (str | Unset):
        ms_token (str | Unset):
        browser_version (str | Unset):
        browser_name (str | Unset):
        field_signature (str | Unset):
        x_bogus (str | Unset):
        user_agent (str | Unset):
    """

    code: float
    message: str | Unset = UNSET
    signed_url: str | Unset = UNSET
    ms_token: str | Unset = UNSET
    browser_version: str | Unset = UNSET
    browser_name: str | Unset = UNSET
    field_signature: str | Unset = UNSET
    x_bogus: str | Unset = UNSET
    user_agent: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        signed_url = self.signed_url

        ms_token = self.ms_token

        browser_version = self.browser_version

        browser_name = self.browser_name

        field_signature = self.field_signature

        x_bogus = self.x_bogus

        user_agent = self.user_agent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if signed_url is not UNSET:
            field_dict["signedUrl"] = signed_url
        if ms_token is not UNSET:
            field_dict["msToken"] = ms_token
        if browser_version is not UNSET:
            field_dict["browserVersion"] = browser_version
        if browser_name is not UNSET:
            field_dict["browserName"] = browser_name
        if field_signature is not UNSET:
            field_dict["_signature"] = field_signature
        if x_bogus is not UNSET:
            field_dict["X-Bogus"] = x_bogus
        if user_agent is not UNSET:
            field_dict["User-Agent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        signed_url = d.pop("signedUrl", UNSET)

        ms_token = d.pop("msToken", UNSET)

        browser_version = d.pop("browserVersion", UNSET)

        browser_name = d.pop("browserName", UNSET)

        field_signature = d.pop("_signature", UNSET)

        x_bogus = d.pop("X-Bogus", UNSET)

        user_agent = d.pop("User-Agent", UNSET)

        get_sign_webcast_url_response = cls(
            code=code,
            message=message,
            signed_url=signed_url,
            ms_token=ms_token,
            browser_version=browser_version,
            browser_name=browser_name,
            field_signature=field_signature,
            x_bogus=x_bogus,
            user_agent=user_agent,
        )

        return get_sign_webcast_url_response
