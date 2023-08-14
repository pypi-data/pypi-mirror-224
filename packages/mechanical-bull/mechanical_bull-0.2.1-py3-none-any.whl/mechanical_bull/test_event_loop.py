import asyncio
from unittest.mock import patch, AsyncMock, MagicMock

from .event_loop import handle_connection


@patch("bovine.BovineClient")
async def test_loop_no_loop(mock_client):
    mock_client.return_value = mock_client

    source = AsyncMock()
    mock_client.event_source = AsyncMock(return_value=source)

    source.__aiter__ = MagicMock(return_value=source)
    source.__anext__ = AsyncMock(return_value=None)

    await handle_connection(mock_client, [])

    mock_client.event_source.assert_awaited_once()


@patch("bovine.BovineClient")
async def test_cancelling_task(mock_client):
    mock_client.return_value = mock_client

    source = AsyncMock()
    mock_client.event_source = AsyncMock(return_value=source)

    source.__aiter__ = MagicMock(return_value=source)
    source.__anext__ = AsyncMock(return_value=MagicMock(data="{}"))

    async def wait_handler(client, data):
        await asyncio.sleep(0.1)

    task = asyncio.create_task(handle_connection(mock_client, [wait_handler]))
    await asyncio.sleep(0.4)
    task.cancel()

    async def wait_and_return(*args):
        await asyncio.sleep(0.1)
        return MagicMock(data="{}")

    source.__anext__ = wait_and_return

    task = asyncio.create_task(handle_connection(mock_client, []))
    await asyncio.sleep(0.4)
    task.cancel()
