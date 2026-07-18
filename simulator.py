import http.server
import socketserver
import os

PORT = 8080

class UniversalOTASimulator(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"\n[+] INTERCEPTED REQUEST from {self.client_address}")
        print(f"    Device requested URL path: {self.path}")
        print(f"    Headers received:\n{self.headers}")
        
        if ".bin" in self.path or ".zip" in self.path or "update" in self.path:
            print("    [!] Target looks like a firmware request! Serving test file...")
            
        return super().do_GET()

os.system('clear')
print(f"==================================================")
print(f"[*] OTA Interceptor Simulator Listening on Port {PORT}")
print(f"[*] Awaiting target device connection...")
print(f"==================================================")

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), UniversalOTASimulator) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Stopping simulator server.")
