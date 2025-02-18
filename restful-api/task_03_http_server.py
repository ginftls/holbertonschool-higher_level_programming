#!/usr/bin/python3
"""Module for RequestHandler class"""


import http.server
import json
from urllib.parse import urlparse


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='text/plain'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()

    def _send_json_response(self, data, status_code=200):
        # Helper method to send JSON responses
        self._set_headers(status_code, 'application/json')
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        # Parse the URL path
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        try:
            # Route requests based on path
            if path == '/':
                # Root endpoint
                self._set_headers()
                response = "Hello, this is a simple API!"
                self.wfile.write(response.encode('utf-8'))

            elif path == '/data':
                # Data endpoint - returns sample JSON data
                sample_data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
                self._send_json_response(sample_data)

            elif path == '/status':
                # Status endpoint
                self._send_json_response({"status": "OK"})

            elif path == '/info':
                # Info endpoint
                info_data = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
                self._send_json_response(info_data)

            else:
                # Handle undefined endpoints
                error_message = {"error": "Endpoint not found"}
                self._send_json_response(error_message, 404)

        except Exception as e:
            # Handle any unexpected errors
            error_message = {"error": str(e)}
            self._send_json_response(error_message, 500)

    def do_OPTIONS(self):
        # Handle OPTIONS requests for CORS
        self._set_headers()


def run_server(port=8000):
    """Start the HTTP server on the specified port."""
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
