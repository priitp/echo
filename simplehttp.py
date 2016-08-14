#!/usr/bin/env python3

# This is basic HTTP echo server. It is mostly usable for inspecting
# incoming requests.
#
# curl -s -H "X-Hello: World!" IP:PORT
#

import http.server
import logging

class EchoHandler(http.server.BaseHTTPRequestHandler):

    # Str8 from the Python logging tutorial.
    logger = logging.getLogger('EchoHandler')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    
    def do_GET(self):
        self.logger.info("Handling GET")
        self.logger.info("request path = '{}'".format(self.path))
        self.logger.info("headers = {}".format(self.headers))
        self.logger.info("GET done.")
        self.send_response(200)
        self.send_header("Set-Cookie", "hello=simplehttp")
        self.end_headers()

    def do_POST(self):
        self.logger.info("Handling POST")
        self.logger.info("request path = '{}'".format(self.path))
        self.logger.info("headers = '{}'".format(self.headers))
        self.logger.info("POST done.")
        self.send_response(200)
        self.end_headers()

    do_DELETE = do_GET
    do_PUT = do_POST

if __name__ == "__main__":
    port = 8080
    server = http.server.HTTPServer(('', port), EchoHandler)
    server.serve_forever()
