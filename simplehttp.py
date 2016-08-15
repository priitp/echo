#!/usr/bin/env python3

# This is basic HTTP echo server. It is mostly usable for inspecting
# incoming requests. Loosely based on this:
# https://gist.github.com/huyng/814831
#
# curl -s -H "X-Hello: World!" IP:PORT
# curl -s -H "X-Hello: World!" -d @some/file IP:PORT
#

import http.server
import logging
import argparse

default_port = 8080
default_interface = ''

class EchoHandler(http.server.BaseHTTPRequestHandler):

    # Str8 from the Python logging tutorial.
    logger = logging.getLogger('EchoHandler')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    def command_handler(self):
        self.logger.info("Handling {}".format(self.command))
        self.logger.info("request path = '{}'".format(self.path))
        self.logger.info("headers = {}".format(self.headers))

        if self.command in {'POST', 'PUT'}:
            content_length = int(self.headers['Content-Length'])
            self.logger.info("POST data = {}".format(self.rfile.read(content_length)))

        self.logger.info("{} done.".format(self.command))
        self.send_response(200)
        self.send_header("Set-Cookie", "hello=simplehttp")
        self.end_headers()

    do_GET = command_handler
    do_POST = command_handler
    do_DELETE = command_handler
    do_PUT = command_handler

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple HTTP echo server.')
    parser.add_argument('-p', dest='port', default=default_port, type=int, help='Port number')
    parser.add_argument('-i', dest='interface', default=default_interface, help='Interface to bind to (default: {})'.format(default_interface))
    args = parser.parse_args()

    server = http.server.HTTPServer((args.interface, args.port), EchoHandler)
    server.serve_forever()
