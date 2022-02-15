from tornado.web import Application

from src.core.dispatcher.handler import DispatcherHandler


def create_app() -> Application:
    app = Application(handlers=[
        (r'/', DispatcherHandler)
    ])

    app.listen(8000)

    return app
