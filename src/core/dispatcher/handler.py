from tornado.web import RequestHandler


class DispatcherHandler(RequestHandler):

    def get(self):
        self.write({'message': 'hello'})
