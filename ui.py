import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page Setup
st.set_page_config(page_title="AI Loan Agent Pro", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🏦 Smart Loan AI Decision Engine")

# --- SIDEBAR: Input Profile ---
with st.sidebar:
    st.header("👤 Customer Data")
    income = st.number_input("Annual Income (₹)", value=100000, step=1000)
    credit_score = st.slider("Credit Score", 300, 850, 750)
    loan_amt = st.number_input("Loan Amount Requested (₹)", value=500000)
    tenure = st.selectbox("Tenure (Years)", [5, 10, 15, 20, 30], index=0)

# --- LOGIC ---
eligibility = (credit_score / 850) * 100
status = "APPROVED" if credit_score >= 600 and loan_amt <= (income * 10) else "REJECTED"

# --- TOP METRICS ---
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Eligibility Score", f"{eligibility:.1f}%", delta="High" if eligibility > 70 else "Low")
with c2:
    color = "green" if status == "APPROVED" else "red"
    st.markdown(f"### Decision: <span style='color:{color}'>{status}</span>", unsafe_allow_html=True)
with c3:
    st.metric("Max Eligible Limit", f"₹{income * 10:,}")

st.divider()

# --- COMPARISON & EMI ---
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("📊 Bank Offers Comparison")
    banks = pd.DataFrame({
        "Bank Name": ["ICICI Bank", "Axis Bank", "HDFC Bank"],
        "Max Limit": [f"₹{income*10.7:,.0f}", f"₹{income*11.7:,.0f}", f"₹{income*9.5:,.0f}"],
        "ROI": ["10.33%", "11.33%", "10.75%"],
        "Rating": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐"]
    })
    st.table(banks)

with col_right:
    st.subheader("💰 EMI Breakdown")
    r = 10.33 / (12 * 100)
    n = tenure * 12
    emi = loan_amt * r * ((1+r)**n) / ((1+r)**n - 1)
    
    st.info(f"**Monthly EMI:** ₹{emi:,.2f}")
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = emi,
        number = {'prefix': "₹"},
        gauge = {'axis': {'range': [0, 50000]}, 'bar': {'color': "#1f77b4"}},
        title = {'text': "Monthly Commitment"}
    ))
    st.plotly_chart(fig, use_container_width=True)

# --- FINAL AI JUSTIFICATION ---
st.subheader("🤖 AI Justification Report")
if status == "APPROVED":
    st.success(f"**Validation Success:** Reward 1.0. Customer is eligible for ₹{loan_amt:,} based on a credit score of {credit_score}. Recommended ICICI at 10.33% ROI.")
else:
    st.error(f"**Validation Failed:** Reward 0.0. Loan amount ₹{loan_amt:,} exceeds limit for current profile.")
 