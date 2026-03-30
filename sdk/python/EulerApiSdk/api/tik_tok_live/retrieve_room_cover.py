from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.json_response import JSONResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    unique_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uniqueId"] = unique_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/room_cover",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | JSONResponse | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Any | JSONResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = JSONResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Any | JSONResponse, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | JSONResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    unique_id: str,
) -> Response[Any | JSONResponse]:
    """Requires Business Plan - Fetch TikTok LIVE Stream Cover URL given a uniqueId.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JSONResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    unique_id: str,
) -> Any | JSONResponse | None:
    """Requires Business Plan - Fetch TikTok LIVE Stream Cover URL given a uniqueId.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JSONResponse
    """

    return sync_detailed(
        client=client,
        unique_id=unique_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    unique_id: str,
) -> Response[Any | JSONResponse]:
    """Requires Business Plan - Fetch TikTok LIVE Stream Cover URL given a uniqueId.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JSONResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    unique_id: str,
) -> Any | JSONResponse | None:
    """Requires Business Plan - Fetch TikTok LIVE Stream Cover URL given a uniqueId.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JSONResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            unique_id=unique_id,
        )
    ).parsed
