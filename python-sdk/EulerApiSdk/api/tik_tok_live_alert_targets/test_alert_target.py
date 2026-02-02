from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.test_alert_target_response import TestAlertTargetResponse
from ...types import Response


def _get_kwargs(
    account_id: float,
    alert_id: float,
    target_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/{account_id}/alerts/{alert_id}/targets/{target_id}/test".format(
            account_id=quote(str(account_id), safe=""),
            alert_id=quote(str(alert_id), safe=""),
            target_id=quote(str(target_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TestAlertTargetResponse | None:
    if response.status_code == 200:
        response_200 = TestAlertTargetResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TestAlertTargetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: float,
    alert_id: float,
    target_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[TestAlertTargetResponse]:
    """Test an alert target

    Args:
        account_id (float):
        alert_id (float):
        target_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestAlertTargetResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
        target_id=target_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    alert_id: float,
    target_id: float,
    *,
    client: AuthenticatedClient,
) -> TestAlertTargetResponse | None:
    """Test an alert target

    Args:
        account_id (float):
        alert_id (float):
        target_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestAlertTargetResponse
    """

    return sync_detailed(
        account_id=account_id,
        alert_id=alert_id,
        target_id=target_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    alert_id: float,
    target_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[TestAlertTargetResponse]:
    """Test an alert target

    Args:
        account_id (float):
        alert_id (float):
        target_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestAlertTargetResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
        target_id=target_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    alert_id: float,
    target_id: float,
    *,
    client: AuthenticatedClient,
) -> TestAlertTargetResponse | None:
    """Test an alert target

    Args:
        account_id (float):
        alert_id (float):
        target_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestAlertTargetResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            alert_id=alert_id,
            target_id=target_id,
            client=client,
        )
    ).parsed
