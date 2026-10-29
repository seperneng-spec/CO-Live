from fastapi import APIRouter

router = APIRouter()


@router.post("/webhooks/shopify")
def shopify_webhook() -> dict:
    return {"status": "received", "provider": "shopify"}


@router.post("/webhooks/tiktok")
def tiktok_webhook() -> dict:
    return {"status": "received", "provider": "tiktok"}
