from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.json_response import JSONResponse
from ...models.sign_tik_tok_url_body import SignTikTokUrlBody
from ...models.sign_tik_tok_url_response import SignTikTokUrlResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["client"] = client_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webcast/sign_url",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JSONResponse | SignTikTokUrlResponse | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> JSONResponse | SignTikTokUrlResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = SignTikTokUrlResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = JSONResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JSONResponse | SignTikTokUrlResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> Response[JSONResponse | SignTikTokUrlResponse]:
    """
    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        body (SignTikTokUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JSONResponse | SignTikTokUrlResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        client_query=client_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> JSONResponse | SignTikTokUrlResponse | None:
    """
    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        body (SignTikTokUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JSONResponse | SignTikTokUrlResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        client_query=client_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> Response[JSONResponse | SignTikTokUrlResponse]:
    """
    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        body (SignTikTokUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JSONResponse | SignTikTokUrlResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        client_query=client_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> JSONResponse | SignTikTokUrlResponse | None:
    """
    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        body (SignTikTokUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JSONResponse | SignTikTokUrlResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            client_query=client_query,
        )
    ).parsed
