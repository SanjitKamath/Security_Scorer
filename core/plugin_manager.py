# File: core/plugin_manager.py

import plugins.os_security as os_sec
import plugins.firewall as fw
import plugins.user_account as ua
import plugins.network as net

class PluginManager:
    def __init__(self):
        self.plugins = [
            os_sec.OSSecurityCheck(),
            fw.FirewallCheck(),
            ua.UserAccountCheck(),
            net.NetworkCheck()
        ]

    def run_all_plugins(self):
        results = []
        for plugin in self.plugins:
            try:
                results.append(plugin.run_check())
            except Exception as e:
                results.append({
                    "name": plugin.__class__.__name__,
                    "result": False,
                    "risk_level": "Unknown",
                    "score_impact": -5,
                    "error": str(e)
                })
        return results
