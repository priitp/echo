#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SimpleHTTPServer
import SocketServer
import logging

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info("Handling GET:")
        logging.info("request path = '{}'".format(self.path))
        logging.info("headers = '{}'".format(self.headers))
        logging.info("GET done.")
        self.send_response(200)
        self.send_cookie("Set-Cookie", "hello=simplehttp")
        self.end_headers()
    def do_POST(self):
        logging.info("Handling POST:")
        logging.info("request path = '{}'".format(self.path))
        logging.info("headers = '{}'".format(self.headers))
        logging.info("GET done.")
        self.send_response(200)
        self.end_headers()
    
if __name__ == "__main__":
    port = 8080
    server = HTTPServer(('', port), EchoHandler)
    server.serve_forever()
