from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlencode
import urllib.request

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the search query from the URL parameter
        query = self.path.split('?')[1]

        # Encode the query
        encoded_query = urlencode({'q': query})

        # Redirect to Google search with the encoded query
        google_url = 'https://www.google.com/search?' + encoded_query
        self.send_response(302)
        self.send_header('Location', google_url)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=ProxyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
