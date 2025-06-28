# plugins/os_security.py

import platform
from plugins.base_plugin import SecurityPlugin

class OSSecurityCheck(SecurityPlugin):
    def run_check(self):
        os_version = platform.version()
        try:
            build_number = float(os_version.split(".")[2])
        except (IndexError, ValueError):
            build_number = 0
        result = build_number >= 19045
        return {
            "name": "OS Version Check",
            "result": result,
            "risk_level": "Medium",
            "score_impact": 10 if result else -10,
            "version": os_version  # ✅ Added version info
        }
