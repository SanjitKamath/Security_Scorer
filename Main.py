# ---------------------------
# main.py
# ---------------------------
from core.plugin_manager import PluginManager
from core.scoring_engine import ScoringEngine
from core.report_generator import ReportGenerator

class SecurityScoreApp:
    def __init__(self):
        self.plugin_manager = PluginManager()
        self.scoring_engine = ScoringEngine()

    def run(self):
        print("Running Security Score Assessment...\n")

        # Run all plugin-based checks
        results = self.plugin_manager.run_all_plugins()

        # Compute security score
        score = self.scoring_engine.compute_score(results)

        # Add reasons and details for medium or high risk levels
        for item in results:
            if item["risk_level"] in ["Medium", "High"]:
                if item["name"] == "OS Version Check":
                    item["reason"] = "OS is outdated. Older versions may have unpatched vulnerabilities."
                    item["details"] = f"Detected OS version: {item.get('version', 'Unknown')}"
                elif item["name"] == "Firewall Status":
                    item["reason"] = "Firewall is disabled. This exposes your system to network attacks."
                    item["details"] = "Enable it via Windows Defender Firewall settings."
                elif item["name"] == "Admin Accounts Check":
                    item["reason"] = "Too many administrator accounts. Increases attack surface."
                    item["details"] = f"Number of admins found: {item.get('admin_count', 'Unknown')}"
                elif item["name"] == "Common Ports Check":
                    item["reason"] = "One or more vulnerable ports are open. Could allow unauthorized access."
                    open_ports = item.get("open_ports", [])
                    item["details"] = f"Open ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}"

        # Generate and display the report
        report = ReportGenerator(results, score)
        report.generate_report()

        # Display reasons and details for risks if available
        for item in results:
            if "reason" in item:
                print(f"Reason for {item['name']} being {item['risk_level']}: {item['reason']}")
            if "details" in item:
                print(f"Details: {item['details']}")

if __name__ == "__main__":
    app = SecurityScoreApp()
    app.run()
