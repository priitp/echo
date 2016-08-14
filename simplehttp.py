#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SimpleHTTPServer
import SocketServer
import logging

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.warning("Handling GET:")
        logging.warning("request path = '{}'".format(self.path))
        logging.warning("headers = {}".format(self.headers))
        logging.warning("GET done.")
        self.send_response(200)
        self.send_header("Set-Cookie", "hello=simplehttp")
        self.end_headers()
    def do_POST(self):
        logging.warning("Handling POST:")
        logging.warning("request path = '{}'".format(self.path))
        logging.warning("headers = '{}'".format(self.headers))
        logging.warning("GET done.")
        self.send_response(200)
        self.end_headers()
    
if __name__ == "__main__":
    port = 8080
    server = HTTPServer(('', port), EchoHandler)
    server.serve_forever()
