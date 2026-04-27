from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webcast_gift_info_route_response import WebcastGiftInfoRouteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    room_id: str,
    webcast_language: str | Unset = "en",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["room_id"] = room_id

    params["webcast_language"] = webcast_language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/gift_info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WebcastGiftInfoRouteResponse | None:
    if response.status_code == 200:
        response_200 = WebcastGiftInfoRouteResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WebcastGiftInfoRouteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    room_id: str,
    webcast_language: str | Unset = "en",
) -> Response[WebcastGiftInfoRouteResponse]:
    """Retrieve TikTok Live Room Gift List

    Args:
        room_id (str):
        webcast_language (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastGiftInfoRouteResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        webcast_language=webcast_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    room_id: str,
    webcast_language: str | Unset = "en",
) -> WebcastGiftInfoRouteResponse | None:
    """Retrieve TikTok Live Room Gift List

    Args:
        room_id (str):
        webcast_language (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastGiftInfoRouteResponse
    """

    return sync_detailed(
        client=client,
        room_id=room_id,
        webcast_language=webcast_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    room_id: str,
    webcast_language: str | Unset = "en",
) -> Response[WebcastGiftInfoRouteResponse]:
    """Retrieve TikTok Live Room Gift List

    Args:
        room_id (str):
        webcast_language (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastGiftInfoRouteResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        webcast_language=webcast_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    room_id: str,
    webcast_language: str | Unset = "en",
) -> WebcastGiftInfoRouteResponse | None:
    """Retrieve TikTok Live Room Gift List

    Args:
        room_id (str):
        webcast_language (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastGiftInfoRouteResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            room_id=room_id,
            webcast_language=webcast_language,
        )
    ).parsed
