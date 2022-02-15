from tornado.web import RequestHandler

from src.integrations.cache.client import Client as CacheClient


class DispatcherHandler(RequestHandler):

    def get(self):
        message = CacheClient().get(
            name='message', default='default_message'
        )
        self.write({'message': message})
