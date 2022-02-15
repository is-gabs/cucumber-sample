from tornado.ioloop import IOLoop

from src.core.app import create_app

if __name__ == '__main__':
    app = create_app()
    IOLoop.current().start()
