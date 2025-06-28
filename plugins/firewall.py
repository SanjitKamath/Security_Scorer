import subprocess
from plugins.base_plugin import SecurityPlugin

class FirewallCheck(SecurityPlugin):
    def run_check(self):
        try:
            output = subprocess.check_output(
                "netsh advfirewall show allprofiles", 
                shell=True,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            ).decode('utf-8', errors='ignore')
            
            # More robust checking of all profiles
            domain_enabled = "Domain Profile Settings" in output and "State ON" in output
            private_enabled = "Private Profile Settings" in output and "State ON" in output
            public_enabled = "Public Profile Settings" in output and "State ON" in output
            
            result = domain_enabled and private_enabled and public_enabled
            
        except subprocess.SubprocessError as e:
            print(f"Error checking firewall status: {e}")
            result = False

        return {
            "name": "Firewall Status",
            "result": result,
            "risk_level": "High",
            "score_impact": 15 if result else -15,
            "details": {
                "domain_profile": domain_enabled,
                "private_profile": private_enabled,
                "public_profile": public_enabled
            }
        }