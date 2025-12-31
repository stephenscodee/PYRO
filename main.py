from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="PYRO AI Brain")

class UserIntent(BaseModel):
    text: str
    user_id: str

class WorkflowStep(BaseModel):
    action: str
    params: dict
    next_step: Optional[str] = None

class GeneratedWorkflow(BaseModel):
    workflow_id: str
    steps: List[WorkflowStep]
    explanation: str

@app.get("/")
async def root():
    return {"message": "PYRO AI Brain is active"}

@app.post("/reason", response_model=GeneratedWorkflow)
async def reason(intent: UserIntent):
    # TODO: Integrate with LLM (GPT/Llama) to parse intent
    # For now, return a mock response
    return GeneratedWorkflow(
        workflow_id="mock-123",
        steps=[
            WorkflowStep(action="gmail.receive_email", params={"filter": "leads"}),
            WorkflowStep(action="whatsapp.send_message", params={"to": "user", "message": "New lead received!"})
        ],
        explanation="Detected intent to handle new leads via email and notify via WhatsApp."
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
