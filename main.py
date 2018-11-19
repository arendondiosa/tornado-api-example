from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web


class Welcome(tornado.web.RequestHandler):
    def get(self):
        response = {
            'ok': True,
            'message':  'Welcome to API'
        }
        self.write(response)


class GetCustomers(tornado.web.RequestHandler):
    def get(self):
        response = {
            'ok': True,
            'data': [
                {'id': 1, 'first_name': 'Sam', 'last_name': 'Smith', 'phone': '333-333-3333',
                    'email': 'ssmith@yahoo.com', 'address': '33 Birch Rd', 'city': 'Miami', 'state': 'FL'},
                {'id': 2, 'first_name': 'Brad', 'last_name': 'Traversy', 'phone': '222-222-2222',
                    'email': 'ssmith@yahoo.com', 'address': '33 Birch Rd', 'city': 'Miami', 'state': 'FL'},
                {'id': 3, 'first_name': 'Sara', 'last_name': 'Tomson', 'phone': '111-111-1111',
                    'email': 'ssmith@yahoo.com', 'address': '33 Birch Rd', 'city': 'Miami', 'state': 'FL'},
                {'id': 4, 'first_name': 'Sam', 'last_name': 'Smith', 'phone': '333-333-3333',
                    'email': 'ssmith@yahoo.com', 'address': '33 Birch Rd', 'city': 'Miami', 'state': 'FL'}
            ]
        }
        self.write(response)


application = tornado.web.Application([
    (r"/api", Welcome),
    # (r"/api/getgamebyid/([0-9]+)", GetGameByIdHandler),
    (r"/api/customers", GetCustomers)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
