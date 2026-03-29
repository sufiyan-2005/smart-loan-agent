import gradio as gr
from env import LoanApprovalEnv
from models import LoanAction
import time


def get_ai_decision(loan_amount, credit_score):
    # Apna environment setup karein
    env = LoanApprovalEnv()
    
    from models import LoanState
    state = LoanState( income=loan_amount * 2, credit_score=credit_score, loan_amount=loan_amount, age=30)
    #state = LoanState(customer_credit_score=credit_score, customer_annual_income=loan_amount)
    
    if credit_score >= 600 and loan_amount <= 500000:
        action_name = "Approve"
    else:
        action_name = "Reject"
        
    action = LoanAction(action=action_name)
    
    offers = []
    if credit_score >= 700:
        offers.append("Axis Bank: Max 1,000,000 at 10.5% ROI")
        offers.append("HDFC Bank: Max 800,000 at 11% ROI")
    elif credit_score >= 600:
        offers.append("ICICI Bank: Max 500,000 at 12.5% ROI")
        
    offers_text = "\n".join(offers) if offers else "No valid offers found."
    
    # Final decision formatting
    decision = f"AI decision based on credit score ({credit_score}): {action_name}"
    
    return offers_text, decision

# --- Gradio UI Design ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🏦 AI Loan Approval Agent")
    gr.Markdown("Apna details daaliye, aur AI ko best decision lene dijiye.")
    
    with gr.Row():
        amount_input = gr.Number(label="Requested Loan Amount (₹)", value=100000)
        score_input = gr.Number(label="Your Credit Score", value=650)
        
    submit_btn = gr.Button("🧠 Ask AI Agent", variant="primary")
    
    with gr.Row():
        offers_output = gr.Textbox(label="Available Bank Offers", lines=4)
        decision_output = gr.Textbox(label="AI Final Decision", lines=2)
        
    # Button action
    submit_btn.click(
        fn=get_ai_decision, 
        inputs=[amount_input, score_input], 
        outputs=[offers_output, decision_output]
    )

if __name__ == "__main__":
    # -----------------------
    demo.launch(server_name="0.0.0.0", server_port=7860)