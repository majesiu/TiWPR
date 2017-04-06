import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Query: "+self.request.query+"<br>")
        self.write("Argument x="+self.get_argument("x","default")+"<br>")
        list1 = self.get_query_arguments("x")
        self.write("Arguments x="+' '.join(list1)+"<br>")

if __name__ == "__main__":
    application = tornado.web.Application([
        ("/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
