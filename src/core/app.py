from tornado.web import Application


def create_app() -> Application:
    app = Application()

    app.listen(8000)

    return app
