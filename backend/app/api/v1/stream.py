from fastapi import APIRouter

router = APIRouter()


@router.post("/stream/start")
def start_stream() -> dict:
    return {"status": "started", "message": "Stream started"}


@router.post("/stream/stop")
def stop_stream() -> dict:
    return {"status": "stopped", "message": "Stream stopped"}
