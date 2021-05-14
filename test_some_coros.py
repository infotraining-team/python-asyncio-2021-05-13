import asyncio
import pytest
import unittest.mock as mock

async def get_value():
    await asyncio.sleep(10)
    return 42

def mock_sleep():
    sleep = mock.AsyncMock(return_value=None)
    return sleep

@pytest.mark.asyncio
async def test_some_results():
    with mock.patch('asyncio.sleep', mock_sleep()):
        res = await get_value()
        assert res == 42
