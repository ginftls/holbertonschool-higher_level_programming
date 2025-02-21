#!/usr/bin/python3
"""Module for fetch_and_print_posts and fetch_and_save_posts methods"""

import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""

        # Default endpoint - root path
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        # Data endpoint - return sample JSON data
        elif self.path == "/data":
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(sample_data).encode())

        # Status endpoint - check API status
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode())

        # Error handling - 404 for undefined endpoints
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


def run_server(port=8000):
    """Start the HTTP server on the specified port"""

    handler = SimpleAPIHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Server running at http://localhost:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
