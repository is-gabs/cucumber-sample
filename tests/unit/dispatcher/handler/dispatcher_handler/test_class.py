from tornado.web import RequestHandler

from src.dispatcher.handler import DispatcherHandler


def test_should_be_request_handler_subclass():
    assert issubclass(DispatcherHandler, RequestHandler)
