from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import auth, stream, webhooks

app = FastAPI(title="CO-Live", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(stream.router, prefix="/api/v1", tags=["stream"])
app.include_router(webhooks.router, prefix="/api/v1", tags=["webhooks"])


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "CO-Live backend"}
