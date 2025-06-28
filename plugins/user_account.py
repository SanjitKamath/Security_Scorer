# plugins/user_account.py

import os
from plugins.base_plugin import SecurityPlugin

class UserAccountCheck(SecurityPlugin):
    def run_check(self):
        try:
            admins = os.popen("net localgroup administrators").read()
            admin_list = [line.strip() for line in admins.splitlines()
                          if line.strip() and not line.startswith(("Alias name", "Comment", "---", "The command completed"))]
            admin_count = len(admin_list)
            result = admin_count <= 5
        except Exception:
            result = False
            admin_count = "Unknown"
        return {
            "name": "Admin Accounts Check",
            "result": result,
            "risk_level": "Medium",
            "score_impact": 10 if result else -10,
            "admin_count": admin_count  # ✅ Added count
        }
