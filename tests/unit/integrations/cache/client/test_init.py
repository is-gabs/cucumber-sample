from unittest import mock

from src.integrations.cache.client import Client


@mock.patch('src.integrations.cache.client.settings')
@mock.patch('src.integrations.cache.client.Redis')
def test_should_populate_client_with_redis_instance(
    mock_redis,
    mock_settings
):
    result = Client()

    mock_redis.assert_called_once_with(
        host=mock_settings.CACHE_HOST,
        port=mock_settings.CACHE_PORT
    )
    assert result._client == mock_redis.return_value
