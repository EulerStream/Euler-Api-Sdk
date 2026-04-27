from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oxy_labs_proxy_region import OxyLabsProxyRegion
from ...models.webcast_feed_route_response import WebcastFeedRouteResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    region: OxyLabsProxyRegion,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_region = region.value
    params["region"] = json_region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/feed",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WebcastFeedRouteResponse | None:
    if response.status_code == 200:
        response_200 = WebcastFeedRouteResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WebcastFeedRouteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    region: OxyLabsProxyRegion,
) -> Response[WebcastFeedRouteResponse]:
    """Requires Premium Routes Addon - Fetch the TikTok LIVE webcast feed for a specific region. Gets a
    random sampling of creators for a region.

    Args:
        region (OxyLabsProxyRegion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastFeedRouteResponse]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    region: OxyLabsProxyRegion,
) -> WebcastFeedRouteResponse | None:
    """Requires Premium Routes Addon - Fetch the TikTok LIVE webcast feed for a specific region. Gets a
    random sampling of creators for a region.

    Args:
        region (OxyLabsProxyRegion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastFeedRouteResponse
    """

    return sync_detailed(
        client=client,
        region=region,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    region: OxyLabsProxyRegion,
) -> Response[WebcastFeedRouteResponse]:
    """Requires Premium Routes Addon - Fetch the TikTok LIVE webcast feed for a specific region. Gets a
    random sampling of creators for a region.

    Args:
        region (OxyLabsProxyRegion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastFeedRouteResponse]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    region: OxyLabsProxyRegion,
) -> WebcastFeedRouteResponse | None:
    """Requires Premium Routes Addon - Fetch the TikTok LIVE webcast feed for a specific region. Gets a
    random sampling of creators for a region.

    Args:
        region (OxyLabsProxyRegion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastFeedRouteResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            region=region,
        )
    ).parsed
