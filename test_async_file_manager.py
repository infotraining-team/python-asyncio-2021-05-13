import inspect
import pytest
import asyncio
import contextlib
import unittest.mock as mock

from async_file_manager import AsyncFile

lines = ["abc\r\n", "def\r\n", "ghi\r\n"]
content = ''.join(lines)

@pytest.mark.asyncio
async def test_AsyncFileCM():
    with mock.patch('builtins.open', mock.mock_open()):
        async with AsyncFile("test_file") as f:
            assert isinstance(f, contextlib.AbstractAsyncContextManager)

@pytest.mark.asyncio
async def test_AsyncFileCM_read_coro():
    with mock.patch('builtins.open', mock.mock_open()):
        async with AsyncFile("test_file") as f:
            assert asyncio.iscoroutinefunction(f.read)

@pytest.mark.asyncio
async def test_AsyncFileCM_read_content():
    with mock.patch('builtins.open', mock.mock_open(read_data=content)):
        async with AsyncFile("test_file") as f:
            data = await f.read()
            assert data == content

@pytest.mark.asyncio
async def test_AsyncFileCM_read_iter():
    with mock.patch('builtins.open', mock.mock_open(read_data=content)):
        got_lines = []
        async with AsyncFile("test_file") as f:
            async for line in f:
                got_lines.append(line)
            assert got_lines == lines