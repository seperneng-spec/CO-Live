from fastapi import APIRouter

router = APIRouter()


@router.get("/auth/health")
def auth_health() -> dict:
    return {"status": "ok", "module": "auth"}


@router.post("/auth/login")
def login() -> dict:
    return {"message": "Login endpoint ready", "token": "demo-token"}
