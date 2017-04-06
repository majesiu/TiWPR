import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/articles" method="post">'
            '<input type="text" name="message">'
            '<input type="submit" value="Add">'
            '</form></body></html>')

class ArticleHandler(tornado.web.RequestHandler):
    articles = []
    def get(self,id1,id2):
        for a in self.articles:
            self.write(a+"<br>")
    def post(self,id1,id2):
        self.articles.append(self.get_argument("message"))
        self.write("OK\n")
    def delete(self,id1,id2):
        self.articles.remove(id2)
        self.write("OK\n")

if __name__ == "__main__":
    application = tornado.web.Application([
        ("/", MainHandler),
        ("/articles(/([0-9]+)?)?", ArticleHandler)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
