from env import LoanApprovalEnv
from models import LoanAction
import threading
import http.server
import socketserver
import json

# --- YE RAHA WO CODE ---
def run_keep_alive_server():
    class OpenEnvAPIHandler(http.server.SimpleHTTPRequestHandler):
        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            dummy_data = {"observation": "Reset OK", "reward": 0.0, "done": False, "info": {}}
            self.wfile.write(json.dumps(dummy_data).encode('utf-8'))

        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "Running"}).encode('utf-8'))

    PORT = 7860
    socketserver.TCPServer.allow_reuse_address = True
    # 👇 YE WALI LINE HAI WO (0.0.0.0 ke saath)
    with socketserver.TCPServer(("0.0.0.0", PORT), OpenEnvAPIHandler) as httpd:
        print(f"🚀 Background Server started on port {PORT}")
        httpd.serve_forever()


threading.Thread(target=run_keep_alive_server, daemon=True).start()
# -----------------------


env = LoanApprovalEnv(difficulty="medium")
state = env.reset()

print("--- CUSTOMER PROFILE ---")
print(f"Score: {state.credit_score} | Income: {state.income:,.2f}")
if state.is_fraud:
    print("⚠️ WARNING: System flagged this profile as HIGH RISK (Fraud)!")

print("\n--- BANK OFFERS FOUND ---")
if not state.available_offers:
    print("No banks interested.")
else:
    for o in state.available_offers:
        print(f"Bank: {o.bank_name} | Max Amount: {o.max_amount:,.2f} | ROI: {o.roi}%")


# --- AI AGENT LOGIC (Thinking Process) ---
if state.is_fraud:
    decision = 0
    reason = "REJECTED: Profile flagged for fraudulent activity. Risk is too high."
elif not state.available_offers:
    decision = 0
    reason = "REJECTED: Credit score is too low, no banks are offering loans."
else:
    decision = 1
    best_bank = min(state.available_offers, key=lambda x: x.roi)
    reason = f"APPROVED: Customer is eligible. Recommended {best_bank.bank_name} at {best_bank.roi}% ROI."

# Action create justification 
action = LoanAction(decision=decision, justification=reason)
next_state, reward, done = env.step(action)

print("\n--- AI AGENT DECISION ---")
print(f"Action: {'Approve' if decision == 1 else 'Reject'}")
print(f"Justification: {action.justification}")
print(f"Reward Received: {reward}")

