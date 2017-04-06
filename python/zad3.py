import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class ArticleHandler(tornado.web.RequestHandler):
    def get(self, id1, id2):
        self.write("Article ID="+id1+id2)

if __name__ == "__main__":
    application = tornado.web.Application([
        ("/", MainHandler),
        ("/articles(/([0-9]+)?)?", ArticleHandler)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
