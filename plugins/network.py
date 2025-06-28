# plugins/network.py

import socket
from plugins.base_plugin import SecurityPlugin

class NetworkCheck(SecurityPlugin):
    def run_check(self):
        open_ports = []
        try:
            ports = [21, 23, 80, 139, 443, 445, 3389]
            for port in ports:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    if sock.connect_ex(("127.0.0.1", port)) == 0:
                        open_ports.append(port)
            result = len(open_ports) == 0
        except Exception:
            result = False
        return {
            "name": "Common Ports Check",
            "result": result,
            "risk_level": "High",
            "score_impact": 15 if result else -15,
            "open_ports": open_ports  # ✅ Added list of ports
        }
