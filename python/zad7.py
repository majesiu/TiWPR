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
    def get(self):
        self.render("07-articles.html", title="List of articles",
                articles=self.articles)
    def post(self):
        self.articles.append(self.get_argument("message"))
        self.write("OK")

if __name__ == "__main__":
    application = tornado.web.Application([
        ("/", MainHandler),
        ("/articles", ArticleHandler)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
