from fastapi import APIRouter

router = APIRouter()


@router.get("/v1")
def root_v1() -> dict:
    return {"message": "CO-Live API v1"}
