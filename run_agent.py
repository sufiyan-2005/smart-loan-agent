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

# Action create karo nayi justification ke saath
action = LoanAction(decision=decision, justification=reason)
next_state, reward, done = env.step(action)

print("\n--- AI AGENT DECISION ---")
print(f"Action: {'Approve' if decision == 1 else 'Reject'}")
print(f"Justification: {action.justification}")
print(f"Reward Received: {reward}")

# --- HUGGING FACE KEEP-ALIVE SERVER ---
import http.server
import socketserver

PORT = 7860
Handler = http.server.SimpleHTTPRequestHandler

print(f"AI Agent Inference Complete! Starting keep-alive server on port {PORT}...")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()


# from env import LoanApprovalEnv
# from models import LoanAction

# env = LoanApprovalEnv(difficulty="medium")
# state = env.reset()

# print("--- CUSTOMER PROFILE ---")
# print(f"Score: {state.credit_score} | Income: {state.income:,.2f}")

# print("\n--- BANK OFFERS FOUND ---")
# if not state.available_offers:
#     print("No banks interested.")
# else:
#     for o in state.available_offers:
#         print(f"Bank: {o.bank_name} | Max: {o.max_amount:,.2f} | ROI: {o.roi}%")

# # Simulation of Agent
# decision = 1 if state.available_offers else 0
# action = LoanAction(decision=decision)
# next_state, reward, done = env.step(action)

# print(f"\nResult: {'Approved' if decision else 'Rejected'} | Reward: {reward}")
