from unittest import mock

from src.core.app import create_app


@mock.patch('src.core.app.Application')
def test_should_return_application_instance(
    mock_application
):
    result = create_app()

    mock_application.assert_called_once_with()
    mock_application.return_value.listen.assert_called_once_with(8000)
    assert result == mock_application.return_value
