class ReportGenerator:
    def __init__(self, results, final_score):
        self.results = results
        self.final_score = final_score

    def generate_report(self):
        print("\nSecurity Scan Report")
        print("=" * 50)
        for item in self.results:
            status = "PASS" if item['result'] else "FAIL"
            print(f"{item['name']}: {status} (Risk: {item['risk_level']})")
            
            # Show reason for Medium or High risk
            if item.get("reason"):
                print(f"  ⚠ Reason: {item['reason']}")
            
            # If an error occurred in plugin execution
            if 'error' in item:
                print(f"  ⚠ Error: {item['error']}")
        
        print("-" * 50)
        print(f"Final Security Score: {self.final_score}/100\n")