#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SimpleHTTPServer
import SocketServer
import logging

class EchoHandler(BaseHTTPRequestHandler):
    logger = logging.getLogger('EchoHandler')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    def do_GET(self):
        self.logger.info("Handling GET:")
        self.logger.info("request path = '{}'".format(self.path))
        self.logger.info("headers = {}".format(self.headers))
        self.logger.info("GET done.")
        self.send_response(200)
        self.send_header("Set-Cookie", "hello=simplehttp")
        self.end_headers()
    def do_POST(self):
        self.logger.info("Handling POST:")
        self.logger.info("request path = '{}'".format(self.path))
        self.logger.info("headers = '{}'".format(self.headers))
        self.logger.info("GET done.")
        self.send_response(200)
        self.end_headers()
    
if __name__ == "__main__":
    port = 8080
    server = HTTPServer(('', port), EchoHandler)
    server.serve_forever()
