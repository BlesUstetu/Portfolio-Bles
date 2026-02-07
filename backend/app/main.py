from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .ai import chat_ai
from .schemas import ChatRequest

app = FastAPI(title="AI Fullstack Chat API")

# Allow local frontend dev (Vite) + easy future deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    reply = chat_ai(req.message)
    return {"reply": reply}
