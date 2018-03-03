import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.template

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/login", LogInHandler),
            (r"/signup", SingUpHandler),
        ]
        super(Application,self).__init__(handlers)

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')

class HomeHandler(BaseHandler):
    def post(self):
        print("Home page handler called")
        self.set_default_headers()
        # loader = tornado.template.Loader(".")
        # self.write(loader.load("index.html").generate())
        # self.render("index.html")


class LogInHandler(BaseHandler):
    def post(self):
        print("LogIn api hit")
        self.set_default_headers()
        username = self.get_argument("user_name")
        password = self.get_argument("password")
        self.write(username+" "+password)



class SingUpHandler(BaseHandler):
    def post(self):
        print("SignUp api hit")
        self.set_default_headers()
        username = self.get_argument("user_name")
        password = self.get_argument("password")
        
        self.write(username+" "+password)




if __name__ == "__main__":
    application = Application()
    app_server = tornado.httpserver.HTTPServer(application)
    app_server.listen(8081)
    print("Application Server started on port 8081 ")
    tornado.ioloop.IOLoop.current().start()
