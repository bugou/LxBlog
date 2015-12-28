import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient


import urllib

from tornado.options import define, options
define("port", default=33333, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
        ]
        settings = {}
        super(Application, self).__init__(handlers, **settings)
        # tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = self.get_argument('wd')
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://www.baidu.com/s?" +
                                urllib.urlencode({"wd": query, }))

        # https://www.baidu.com/s?wd=python

        self.write("""
<div style="text-align: center">
    <div style="font-size: 20px">%s</div>
    <div style="font-size: 20px">%s</div>
</div>""" % (query, response))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    # app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    # http_server = tornado.httpserver.HTTPServer(app)
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
