import http.server
import socketserver
import os
from datetime import datetime

PORT = 8080
LOG_FILE = "logs.txt"

class UniversalOTASimulator(http.server.SimpleHTTPRequestHandler):
    def log_to_file(self, text):
        with open(LOG_FILE, "a") as f:
            f.write(text + "\n")

    def do_GET(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Pull just the client's IP address and append the server port
        client_ip = self.client_address[0]
        
        log_entry = (
            f"\n==================================================\n"
            f"[+] INTERCEPTED REQUEST | {timestamp}\n"
            f"    From Client: {client_ip}:{PORT}\n"
            f"    Requested URL Path: {self.path}\n"
            f"    Headers received:\n{self.headers}"
        )
        
        if ".bin" in self.path or ".zip" in self.path or "update" in self.path:
            log_entry += "    [!] Target looks like a firmware request! Serving test file...\n"

        log_entry += "==================================================\n"

        print(log_entry)
        self.log_to_file(log_entry)
            
        return super().do_GET()

os.system('clear')
print(f"==================================================")
print(f"[*] OTA Interceptor Simulator Listening on Port {PORT}")
print(f"[*] Logging all traffic to: {LOG_FILE}")
print(f"[*] Awaiting target device connection...")
print(f"==================================================")

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), UniversalOTASimulator) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Stopping simulator server.")
