import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = "."

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def run_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"==================================================")
        print(f"  Duhan Tours & Travels Analytics Dashboard")
        print(f"  Server started at: http://localhost:{PORT}")
        print(f"==================================================")
        print(f"Opening dashboard in your web browser...")
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped successfully.")

if __name__ == "__main__":
    run_server()