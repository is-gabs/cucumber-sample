from unittest import mock

from pytest import fixture

from src.integrations.cache.client import Client


@fixture(autouse=True)
def mock_redis():
    with mock.patch(
        'src.integrations.cache.client.Redis'
    ) as mocked:
        yield mocked


@fixture()
def cache_client():
    client = Client()
    client._client = mock.MagicMock()
    yield client
