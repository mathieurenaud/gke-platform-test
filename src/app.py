#print "5678"

import SimpleHTTPServer
import BaseHTTPServer
import SocketServer

## Override base request handler with my own
class PlatformTestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, "OK")
        self.send_header("Content-Type", "text/text")
        self.send_header("Server", "AppDirect/Test")
        self.end_headers()
        self.wfile.write("Hello AppDirect Platform\n")
    # repeat for POST and PUT
    def do_POST(self):
        self.send_response(200, "OK")
        self.send_header("Content-Type", "text/text")
        self.send_header("Server", "AppDirect/Test")
        self.end_headers()
        self.wfile.write("Hello AppDirect Platform\n")
    def do_PUT(self):
        self.send_response(200, "OK")
        self.send_header("Content-Type", "text/text")
        self.send_header("Server", "AppDirect/Test")
        self.end_headers()
        self.wfile.write("Hello AppDirect Platform\n")

PORT = 8000

Handler = PlatformTestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Starting to serve at port ", PORT
httpd.serve_forever()

