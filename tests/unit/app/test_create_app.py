from unittest import mock

from src.app import create_app
from src.dispatcher.handler import DispatcherHandler


@mock.patch('src.app.Application')
def test_should_return_application_instance(
    mock_application
):
    result = create_app()

    mock_application.assert_called_once_with(handlers=[
        (r'/', DispatcherHandler)
    ])
    mock_application.return_value.listen.assert_called_once_with(8000)
    assert result == mock_application.return_value
