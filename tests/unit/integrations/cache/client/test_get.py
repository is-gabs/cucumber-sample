from redis import RedisError


def test_should_return_client_get_value(
    cache_client
):
    mock_client = cache_client._client

    result = cache_client.get(name='name')

    mock_client.get.assert_called_once_with(name='name')
    assert result == mock_client.get.return_value


def test_should_return_default_when_raise_redis_error(
    cache_client
):
    mock_client = cache_client._client
    mock_client.get.side_effect = RedisError

    result = cache_client.get(name='name', default='default')

    assert result == 'default'
