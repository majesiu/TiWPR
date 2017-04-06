import tornado.ioloop
import tornado.web
import datetime
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self,id):
        if not id:
            self.set_status(303)
            self.set_header("Content-Type", "text/plain")
            self.add_header("Location", "/44")
            self.add_header("X-Example-Counter", 10)
            self.set_cookie("counter", "1", "localhost",
                    datetime.datetime.utcnow() + datetime.timedelta(minutes=2))
            self.write("The resource is available somewhere else\n")
        else:
            self.write("That's it!\n")
            self.flush()
            time.sleep(2)
            self.write("Done\n")

if __name__ == "__main__":
    application = tornado.web.Application([
        ("/([0-9]+)?", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
