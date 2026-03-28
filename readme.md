#  Smart-Loan-Agent

##  Project Overview
The **Smart Loan Agent** is an intelligent, AI-driven application designed to streamline and assist with loan-related inquiries and processing. Powered by Google's Generative AI (Gemini) and structured with Pydantic, this agent processes user inputs intelligently to provide accurate, context-aware financial assistance.

This project is fully containerized using Docker and optimized for seamless deployment on cloud platforms like Hugging Face Spaces.

##  Key Features
*  Advanced AI Capabilities:** Utilizes `google-generativeai` for natural language understanding and intelligent responses.
*  Containerized Architecture:** Dockerized environment ensures consistent execution across different platforms.
*  Robust Data Validation:** Uses `pydantic` for strict data parsing and validation.
*  Cloud-Ready Deployment:** Configured to run flawlessly on Hugging Face Spaces (Port 7860, non-root user setup).

##  Project Structure
* `run_agent.py`: The main entry point for the application.
* `models.py`: Contains Pydantic data models for structured data handling.
* `env.py`: Manages environment variables and API keys.
* `requirements.txt`: Project dependencies.
* `Dockerfile`: Instructions for containerizing the application.

##  Local Setup & Installation

Follow these steps to run the Smart Loan Agent on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/smart-loan-agent.git](https://github.com/your-username/smart-loan-agent.git)
   cd smart-loan-agent
