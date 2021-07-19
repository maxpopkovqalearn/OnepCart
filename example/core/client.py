from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop


class MainHandler(RequestHandler):
    """Render the page"""
    def get(self):
        self.render("pages/sample.html")


app = Application([
    (r"/", MainHandler),
])

app.listen(8000)
IOLoop.current().start()
