import http.server
import socketserver

PORT = 8000

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
