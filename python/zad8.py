import tornado.ioloop
import tornado.web
import http.client

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status, **kwargs):
        self.write("HTTP error code: {} {}\n".format(str(status),
                http.client.responses[status]))

class ErrorHandler(tornado.web.ErrorHandler, BaseHandler):
    pass

class MainHandler(BaseHandler):
    def get(self,id):
        rc = int(self.get_argument("rc",200))
        if rc != 200:
            raise tornado.web.HTTPError(rc)
        self.write("Article {}\n".format(id))

if __name__ == "__main__":
    settings = {
        "autoreload": True,
        "debug": True,
        "default_handler_class": ErrorHandler,
        'default_handler_args': dict(status_code=404)
    }
    application = tornado.web.Application([
        ("/([0-9]+)", MainHandler),
        ], **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
