from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webcast_room_chat_payload import WebcastRoomChatPayload
from ...models.webcast_room_chat_payload_v1 import WebcastRoomChatPayloadV1
from ...models.webcast_room_chat_route_response import WebcastRoomChatRouteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    if not isinstance(x_cookie_header, Unset):
        headers["x-cookie-header"] = x_cookie_header

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webcast/chat",
    }

    if isinstance(body, WebcastRoomChatPayloadV1):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WebcastRoomChatRouteResponse | None:
    if response.status_code == 200:
        response_200 = WebcastRoomChatRouteResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WebcastRoomChatRouteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[WebcastRoomChatRouteResponse]:
    """Requires Premium Routes Addon - Send a chat to a TikTok LIVE room.

    Either `targetRoomId` or `targetUniqueId` must be provided to identify the room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (WebcastRoomChatPayload | WebcastRoomChatPayloadV1): The payload configuration for
            sending a chat

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastRoomChatRouteResponse]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> WebcastRoomChatRouteResponse | None:
    """Requires Premium Routes Addon - Send a chat to a TikTok LIVE room.

    Either `targetRoomId` or `targetUniqueId` must be provided to identify the room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (WebcastRoomChatPayload | WebcastRoomChatPayloadV1): The payload configuration for
            sending a chat

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastRoomChatRouteResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[WebcastRoomChatRouteResponse]:
    """Requires Premium Routes Addon - Send a chat to a TikTok LIVE room.

    Either `targetRoomId` or `targetUniqueId` must be provided to identify the room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (WebcastRoomChatPayload | WebcastRoomChatPayloadV1): The payload configuration for
            sending a chat

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastRoomChatRouteResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> WebcastRoomChatRouteResponse | None:
    """Requires Premium Routes Addon - Send a chat to a TikTok LIVE room.

    Either `targetRoomId` or `targetUniqueId` must be provided to identify the room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (WebcastRoomChatPayload | WebcastRoomChatPayloadV1): The payload configuration for
            sending a chat

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastRoomChatRouteResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed
