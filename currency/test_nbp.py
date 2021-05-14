import pytest
from nbp import starting_point
import unittest.mock as mock

response = {'code': 'EUR', 'currency': 'euro', 'rates': [{'effectiveDate': '2021-05-13', 'mid': 4.5447, 'no': '091/A/NBP/2021'}], 'table': 'A'}

def mock_get(data):
    response = mock.Mock()
    response.json = mock.AsyncMock(return_value=data)
    response.status = 200
    session = mock.MagicMock()
    session.return_value.__aenter__ = mock.AsyncMock(return_value=response)
    return session

@pytest.mark.asyncio
async def test_starting_point():
    with mock.patch("aiohttp.ClientSession.get", mock_get(response)):
        res = await starting_point()
        assert res == response
