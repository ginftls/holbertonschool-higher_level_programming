#!/usr/bin/env python3
"""
A simple HTTP server implementation using Python's http.server module.

This server provides basic endpoints for learning web programming concepts:
- GET /: Returns a welcome message
- GET /data: Returns sample JSON data
- GET /status: Returns API status
- Any other endpoint returns a 404 error
"""


import http.server
import json
import sys
from typing import Dict, Any
from http import HTTPStatus


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handler for the Simple API Server.
    Implements basic routing and response handling for
    a learning-focused HTTP server.
    Supports GET requests with JSON responses and proper error handling.
    """

    def _send_response(self,
                       status_code: int = HTTPStatus.OK,
                       content_type: str = 'text/plain',
                       content: str = '') -> None:
        """Helper method to send HTTP responses with proper headers.

        Args:
            status_code: HTTP status code to return
            content_type: MIME type of the response content
            content: The response body
        """
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def _send_json(self,
                   data: Dict[str, Any],
                   status_code: int = HTTPStatus.OK) -> None:
        """Helper method specifically for sending JSON responses.

        Args:
            data: Dictionary to be converted to JSON
            status_code: HTTP status code to return
        """
        json_content = json.dumps(data, indent=2)
        self._send_response(
            status_code=status_code,
            content_type='application/json',
            content=json_content
        )

    def do_GET(self) -> None:
        """Handle GET requests.

        Routes requests to appropriate handlers based on the path.
        Implements endpoints specified in the requirements.
        """
        try:
            # Route the request based on path
            if self.path == '/':
                self._send_response(
                    content="Hello, this is a simple API!"
                )

            elif self.path == '/data':
                sample_data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
                self._send_json(sample_data)

            elif self.path == '/status':
                self._send_json({"status": "OK"})

            else:
                # Handle undefined endpoints with 404
                error_msg = {"error": "Endpoint not found"}
                self._send_json(error_msg, HTTPStatus.NOT_FOUND)

        except Exception as e:
            # Handle unexpected errors with 500
            error_msg = {"error": f"Internal server error: {str(e)}"}
            self._send_json(error_msg, HTTPStatus.INTERNAL_SERVER_ERROR)


def main() -> None:
    """Main function to start the server."""
    try:
        # Configure server
        port = 8000
        server_address = ('', port)
        httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)

        # Start server
        print(f"Starting HTTP server on port {port}...")
        print(f"Try these endpoints:")
        print(f"  http://localhost:{port}/")
        print(f"  http://localhost:{port}/data")
        print(f"  http://localhost:{port}/status")
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()
        sys.exit(0)
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
