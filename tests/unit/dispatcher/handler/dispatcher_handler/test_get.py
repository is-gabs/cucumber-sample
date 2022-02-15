from unittest import mock

from src.dispatcher.handler import DispatcherHandler


@mock.patch('src.dispatcher.handler.CacheClient')
@mock.patch.object(DispatcherHandler, 'write')
def test_should_call_write_method_from_cache(
    mock_write,
    mock_cache_client
):
    mock_get = mock_cache_client.return_value.get

    DispatcherHandler(
        application=mock.MagicMock(),
        request=mock.MagicMock()
    ).get()

    mock_cache_client.assert_called_once_with()
    mock_get.assert_called_once_with(
        name='message',
        default='default_message'
    )
    mock_write.assert_called_once_with({'message': mock_get.return_value})
