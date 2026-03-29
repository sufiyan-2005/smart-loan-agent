
from fastapi import FastAPI
import uvicorn
from .environment import LoanEnvironment

# FastAPI app banayi
app = FastAPI(title="Loan Agent OpenEnv Server")

# Environment load kiya
env = LoanEnvironment()

@app.get("/")
def read_root():
    return {"status": "🚀 FastAPI Server is running successfully!"}

@app.post("/reset")
def reset_environment():
    result = env.reset()
    return {"message": "Environment reset", "data": result}

@app.post("/step")
def step_environment(action: dict):
    result = env.step(action)
    return {"message": "Action processed", "data": result}

def main():
    print("Starting FastAPI server on port 8000...")
    # Bot ye main() function call karega
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
