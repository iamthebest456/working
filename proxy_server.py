from http.server import BaseHTTPRequestHandler, HTTPServer

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the HTML file
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        # Handle search requests
        else:
            parsed_url = urlparse(self.path)
            query = parsed_url.query

            # Redirect to Google search with the query
            google_url = 'https://www.google.com/search?' + query
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
