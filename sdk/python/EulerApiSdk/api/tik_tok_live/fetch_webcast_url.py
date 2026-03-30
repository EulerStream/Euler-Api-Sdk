from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.soax_proxy_region import SoaxProxyRegion
from ...models.uint_8_array import Uint8Array
from ...models.webcast_fetch_platform import WebcastFetchPlatform
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_query: str | Unset = "ttlive-other",
    room_id: str | Unset = UNSET,
    unique_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    country: SoaxProxyRegion | Unset = UNSET,
    platform: WebcastFetchPlatform | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    if not isinstance(x_cookie_header, Unset):
        headers["x-cookie-header"] = x_cookie_header

    params: dict[str, Any] = {}

    params["client"] = client_query

    params["room_id"] = room_id

    params["unique_id"] = unique_id

    params["cursor"] = cursor

    params["user_agent"] = user_agent

    params["client_enter"] = client_enter

    json_country: str | Unset = UNSET
    if not isinstance(country, Unset):
        json_country = country.value

    params["country"] = json_country

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    params["session_id"] = session_id

    params["tt_target_idc"] = tt_target_idc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/fetch",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Uint8Array | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Any | Uint8Array:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = Uint8Array.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Any | Uint8Array, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Uint8Array]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    client_query: str | Unset = "ttlive-other",
    room_id: str | Unset = UNSET,
    unique_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    country: SoaxProxyRegion | Unset = UNSET,
    platform: WebcastFetchPlatform | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[Any | Uint8Array]:
    """Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room ID.

    **Authentication (Optional):** Anonymous access is supported. For authenticated requests, provide
    exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        room_id (str | Unset):
        unique_id (str | Unset):
        cursor (str | Unset):
        user_agent (str | Unset):
        client_enter (bool | Unset):  Default: True.
        country (SoaxProxyRegion | Unset):
        platform (WebcastFetchPlatform | Unset):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Uint8Array]
    """

    kwargs = _get_kwargs(
        client_query=client_query,
        room_id=room_id,
        unique_id=unique_id,
        cursor=cursor,
        user_agent=user_agent,
        client_enter=client_enter,
        country=country,
        platform=platform,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    client_query: str | Unset = "ttlive-other",
    room_id: str | Unset = UNSET,
    unique_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    country: SoaxProxyRegion | Unset = UNSET,
    platform: WebcastFetchPlatform | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Any | Uint8Array | None:
    """Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room ID.

    **Authentication (Optional):** Anonymous access is supported. For authenticated requests, provide
    exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        room_id (str | Unset):
        unique_id (str | Unset):
        cursor (str | Unset):
        user_agent (str | Unset):
        client_enter (bool | Unset):  Default: True.
        country (SoaxProxyRegion | Unset):
        platform (WebcastFetchPlatform | Unset):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Uint8Array
    """

    return sync_detailed(
        client=client,
        client_query=client_query,
        room_id=room_id,
        unique_id=unique_id,
        cursor=cursor,
        user_agent=user_agent,
        client_enter=client_enter,
        country=country,
        platform=platform,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    client_query: str | Unset = "ttlive-other",
    room_id: str | Unset = UNSET,
    unique_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    country: SoaxProxyRegion | Unset = UNSET,
    platform: WebcastFetchPlatform | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[Any | Uint8Array]:
    """Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room ID.

    **Authentication (Optional):** Anonymous access is supported. For authenticated requests, provide
    exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        room_id (str | Unset):
        unique_id (str | Unset):
        cursor (str | Unset):
        user_agent (str | Unset):
        client_enter (bool | Unset):  Default: True.
        country (SoaxProxyRegion | Unset):
        platform (WebcastFetchPlatform | Unset):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Uint8Array]
    """

    kwargs = _get_kwargs(
        client_query=client_query,
        room_id=room_id,
        unique_id=unique_id,
        cursor=cursor,
        user_agent=user_agent,
        client_enter=client_enter,
        country=country,
        platform=platform,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    client_query: str | Unset = "ttlive-other",
    room_id: str | Unset = UNSET,
    unique_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    country: SoaxProxyRegion | Unset = UNSET,
    platform: WebcastFetchPlatform | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Any | Uint8Array | None:
    """Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room ID.

    **Authentication (Optional):** Anonymous access is supported. For authenticated requests, provide
    exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        room_id (str | Unset):
        unique_id (str | Unset):
        cursor (str | Unset):
        user_agent (str | Unset):
        client_enter (bool | Unset):  Default: True.
        country (SoaxProxyRegion | Unset):
        platform (WebcastFetchPlatform | Unset):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Uint8Array
    """

    return (
        await asyncio_detailed(
            client=client,
            client_query=client_query,
            room_id=room_id,
            unique_id=unique_id,
            cursor=cursor,
            user_agent=user_agent,
            client_enter=client_enter,
            country=country,
            platform=platform,
            session_id=session_id,
            tt_target_idc=tt_target_idc,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed
