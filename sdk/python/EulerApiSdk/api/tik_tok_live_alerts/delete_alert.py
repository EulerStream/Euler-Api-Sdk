from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_alert_response import DeleteAlertResponse
from ...types import Response


def _get_kwargs(
    account_id: float,
    alert_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/accounts/{account_id}/alerts/{alert_id}/delete".format(
            account_id=quote(str(account_id), safe=""),
            alert_id=quote(str(alert_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteAlertResponse | None:
    if response.status_code == 200:
        response_200 = DeleteAlertResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteAlertResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteAlertResponse]:
    """Delete an alert from the Sign API

    Args:
        account_id (float):
        alert_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAlertResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
) -> DeleteAlertResponse | None:
    """Delete an alert from the Sign API

    Args:
        account_id (float):
        alert_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAlertResponse
    """

    return sync_detailed(
        account_id=account_id,
        alert_id=alert_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteAlertResponse]:
    """Delete an alert from the Sign API

    Args:
        account_id (float):
        alert_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAlertResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
) -> DeleteAlertResponse | None:
    """Delete an alert from the Sign API

    Args:
        account_id (float):
        alert_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAlertResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            alert_id=alert_id,
            client=client,
        )
    ).parsed
