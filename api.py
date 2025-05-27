from fastapi import FastAPI
from tutor_agent import TutorAgent
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use ["*"] to allow all (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
tutor_agent = TutorAgent()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_tutor(req: QuestionRequest):
    print(req.question)
    response = tutor_agent.route_query(req.question)
    return {"response": response}