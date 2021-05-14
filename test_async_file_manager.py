import pytest
import asyncio
import contextlib
import unittest.mock as mock

from async_file_manager import AsyncFile

@pytest.mark.asyncio
async def test_AsyncFileCM():
    with mock.patch('builtins.open', mock.mock_open()):
        async with AsyncFile("test_file") as f:
            assert isinstance(f, contextlib.AbstractAsyncContextManager)
