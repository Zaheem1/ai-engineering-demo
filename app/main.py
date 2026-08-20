from fastapi import FastAPI

from app.ai.router import router as ai_router

app = FastAPI(title="AI Engineering Demo")

app.include_router(ai_router, prefix="/ai", tags=["ai"])


@app.get("/health")
async def health():
    return {"status": "ok"}
