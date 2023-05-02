from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><head><title>My Server</title></head>')
        self.wfile.write(b'<body><p>This is my server!</p>')
        self.wfile.write(b'</body></html>')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        if 'url' in params:
            url = params['url'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<html><head><title>My Server</title></head>'.encode('utf-8'))
            self.wfile.write(f'<body><p>Received URL: {url}</p>'.encode('utf-8'))
            self.wfile.write(b'</body></html>')
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>My Server</title></head>')
            self.wfile.write(b'<body><p>Bad Request: URL parameter not found</p>')
            self.wfile.write(b'</body></html>')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
