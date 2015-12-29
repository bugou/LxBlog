import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.httpclient

import urllib

from tornado.options import define, options
define("port", default=33333, help="run on given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        query = self.get_argument("wd")
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://www.baidu.com/s?" + urllib.urlencode(
                                                {"wd": query, }
                                                ),
                     callback=self.on_response)

    def on_response(self, response):
        query = self.get_argument("wd")
        self.write("""
<div style="text-align: center">
    <div style="font-size: 20px">%s</div>
    <div style="font-size: 20px">%s</div>
</div>""" % (query, response))
        self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/', IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

