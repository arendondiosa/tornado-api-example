from datetime import date
import tornado.httpserver
import tornado.escape
import tornado.ioloop
import tornado.web
import os

response = {
    'data': [
        {'id': 1, 'first_name': 'Sam', 'last_name': 'Smith', 'phone': '333-333-3333',
         'email': 'ssmith@yahoo.com', 'address': '33 Birch Rd', 'city': 'Miami', 'state': 'FL'},
        {'id': 2, 'first_name': 'Brad', 'last_name': 'Traversy', 'phone': '222-222-2222',
         'email': 'ssmith@yahoo.com', 'address': '33 Birch Rd', 'city': 'Miami', 'state': 'FL'},
        {'id': 3, 'first_name': 'Sara', 'last_name': 'Tomson', 'phone': '111-111-1111',
         'email': 'ssmith@yahoo.com', 'address': '33 Birch Rd', 'city': 'Miami', 'state': 'FL'},
        {'id': 4, 'first_name': 'Laura', 'last_name': 'Rendon', 'phone': '333-444-4444',
         'email': 'lrendon@gmail.com', 'address': '33 Birch Rd', 'city': 'Pereira', 'state': 'RIS'}
    ]
}


class BaseHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods',
                        ' PUT, DELETE, OPTIONS')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class Welcome(BaseHandler):
    def get(self):
        self.write({
            'status': 200,
            'data': 'Welcome to API'
        })

class GetCustomers(BaseHandler):
    def get(self):
        self.write({
            'status': 200,
            'data': response
        })

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        username, designation = data

        global response

        response['data'].append(
            {'id': 'x', 'first_name': username, 'last_name': designation})

        self.write({
            'status': 200,
            'data': response
        })


application = tornado.web.Application([
    (r"/api", Welcome),
    # (r"/api/getgamebyid/([0-9]+)", GetGameByIdHandler),
    (r"/api/customers", GetCustomers)
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 8888))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
