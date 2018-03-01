import tornado.ioloop
import tornado.web
import tornado.httpserver

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/login", LogInHandler),
            (r"/singup", SingUpHandler),
        ]
        super(Application,self).__init__(handlers)

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')

    

if __name__ == "__main__":
    application = Application()
    app_server = tornado.httpserver.HTTPServer(application)
    app_server.listen(8081)
    print("Application Server started on port 8081 ")
    tornado.ioloop.IOLoop.current().start()
