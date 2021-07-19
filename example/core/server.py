import tornado.ioloop
import tornado.web
import os
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        """Success auth"""
        self.write("Hello, ntech!")


class AuthHandler(tornado.web.RequestHandler):

    def check_permission(self, password, username):
        """Check couples user/password"""
        os.chdir(os.path.dirname(__file__))
        user_path = os.path.abspath('users.json')

        with open(user_path) as user_file:
            json_data = json.load(user_file)

        user_name = json_data['login']
        user_password = json_data['password']

        if username == user_name and password == user_password:
            return True
        return False

    def post(self):
        """Authentication"""
        login = self.get_argument('login')
        password = self.get_argument('password')
        auth = self.check_permission(password, login)
        if auth:
            self.redirect(self.get_argument("next", u"/"))
        else:
            self.write("Incorrect")


def make_app():
    """App"""
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/auth", AuthHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8003)
    tornado.ioloop.IOLoop.current().start()
