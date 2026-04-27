from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_jwt_response import CreateJWTResponse
from ...models.jwt_create_config import JWTCreateConfig
from ...types import Response


def _get_kwargs(
    account_id: float,
    *,
    body: JWTCreateConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/{account_id}/jwt/create".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateJWTResponse | None:
    if response.status_code == 200:
        response_200 = CreateJWTResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateJWTResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: JWTCreateConfig,
) -> Response[CreateJWTResponse]:
    """Create a JWT for a given API key. Note that these JWT keys are only valid for the non-authenticated
    Webcast endpoints.
    They function to attach the rate limits of the API key to the request for client-sided applications.

    Args:
        account_id (float):
        body (JWTCreateConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateJWTResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: JWTCreateConfig,
) -> CreateJWTResponse | None:
    """Create a JWT for a given API key. Note that these JWT keys are only valid for the non-authenticated
    Webcast endpoints.
    They function to attach the rate limits of the API key to the request for client-sided applications.

    Args:
        account_id (float):
        body (JWTCreateConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateJWTResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: JWTCreateConfig,
) -> Response[CreateJWTResponse]:
    """Create a JWT for a given API key. Note that these JWT keys are only valid for the non-authenticated
    Webcast endpoints.
    They function to attach the rate limits of the API key to the request for client-sided applications.

    Args:
        account_id (float):
        body (JWTCreateConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateJWTResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: JWTCreateConfig,
) -> CreateJWTResponse | None:
    """Create a JWT for a given API key. Note that these JWT keys are only valid for the non-authenticated
    Webcast endpoints.
    They function to attach the rate limits of the API key to the request for client-sided applications.

    Args:
        account_id (float):
        body (JWTCreateConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateJWTResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
