from tornado.web import Application


def create_app() -> Application:
    app = Application(handlers=[])

    app.listen(8000)

    return app
