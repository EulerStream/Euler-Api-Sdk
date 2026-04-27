from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.o_auth_revoke_response import OAuthRevokeResponse
from ...models.revoke_request_body import RevokeRequestBody
from ...types import Response


def _get_kwargs(
    *,
    body: RevokeRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/oauth/revoke",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OAuthRevokeResponse | None:
    if response.status_code == 200:
        response_200 = OAuthRevokeResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OAuthRevokeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RevokeRequestBody,
) -> Response[OAuthRevokeResponse]:
    """Revoke an access token or refresh token (RFC 7009).
    This endpoint always returns success for valid client credentials,
    even if the token was already revoked or invalid.

    Args:
        body (RevokeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuthRevokeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RevokeRequestBody,
) -> OAuthRevokeResponse | None:
    """Revoke an access token or refresh token (RFC 7009).
    This endpoint always returns success for valid client credentials,
    even if the token was already revoked or invalid.

    Args:
        body (RevokeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuthRevokeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RevokeRequestBody,
) -> Response[OAuthRevokeResponse]:
    """Revoke an access token or refresh token (RFC 7009).
    This endpoint always returns success for valid client credentials,
    even if the token was already revoked or invalid.

    Args:
        body (RevokeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuthRevokeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RevokeRequestBody,
) -> OAuthRevokeResponse | None:
    """Revoke an access token or refresh token (RFC 7009).
    This endpoint always returns success for valid client credentials,
    even if the token was already revoked or invalid.

    Args:
        body (RevokeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuthRevokeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
