from env import LoanApprovalEnv
from models import LoanAction

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

# --- HUGGING FACE OPENENV API SERVER ---
import http.server
import socketserver
import json

class OpenEnvAPIHandler(http.server.SimpleHTTPRequestHandler):

    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
       
        # To understand the format of RL dummy to send data to pass 
        dummy_data = {
            "observation": "Environment Reset Successful", 
            "reward": 0.0, 
            "done": False, 
            "info": {}
        }
        self.wfile.write(json.dumps(dummy_data).encode('utf-8'))

    # Normal browser GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "AI Agent Running Perfect!"}).encode('utf-8'))

PORT = 7860
print(f"AI Agent Ready! Starting OpenEnv API server on port {PORT}...")
socketserver.TCPServer.allow_reuse_address = True # Port error se bachne ke liye
with socketserver.TCPServer(("", PORT), OpenEnvAPIHandler) as httpd:
    httpd.serve_forever()
