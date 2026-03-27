# 🏦 AI Smart Loan Approval Environment (OpenEnv)

Ek real-world AI environment jo applicant ke credit score aur income ke basis par loan approve karta hai aur best **Bank Offers (ROI & Max Amount)** suggest karta hai.

## 🌟 Key Features
- **Smart Logic:** Sirf reject/approve nahi, balki multiple banks se live ROI fetch karta hai.
- **Bank Matchmaking:** HDFC, SBI, ICICI, aur Axis banks ke dynamic offers.
- **Difficulty Levels:** - **Easy:** Base credit score check.
  - **Medium:** Income-to-loan ratio analysis.
  - **Hard:** Fraud detection logic.
- **OpenEnv Spec:** Purely compatible with `step()`, `reset()`, and `state()` methods.

## 🛠️ Project Structure
- `env.py`: Core logic for loan evaluation and bank offers.
- `models.py`: Pydantic models for Typed data.
- `openenv.yaml`: Environment configuration.
- `run_agent.py`: Testing script to run the environment.
- `Dockerfile`: For easy deployment on Hugging Face Spaces.

## 🚀 How to Run (Step-by-Step)

### 1. Requirements Install Karein
Sabse pehle terminal kholo aur ye command chalao:
```bash
pip install pydantic pyyaml