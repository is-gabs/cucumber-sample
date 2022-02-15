from unittest import mock

from src.core.dispatcher.handler import DispatcherHandler


@mock.patch.object(DispatcherHandler, 'write')
def test_should_call_write_method(mock_write):

    DispatcherHandler(
        application=mock.MagicMock(),
        request=mock.MagicMock()
    ).get()

    mock_write.assert_called_once_with()
