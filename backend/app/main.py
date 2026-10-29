import asyncio
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal, ClientModel, init_db

init_db()
app = FastAPI(title="CO-Live Commercial Streaming Engine", version="1.0.0")
connected_clients = set()

class StreamTriggerPayload(BaseModel):
    api_key: str
    action_type: str  # intro_product, pitch_features, order_alert
    product_name: str
    custom_message: str = ""
    target_customer: str = ""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.websocket("/ws/broadcast")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

@app.post("/api/v1/stream/trigger")
async def trigger_stream(payload: StreamTriggerPayload, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.api_key == payload.api_key).first()
    if not client:
        raise HTTPException(status_code=401, detail="API Key ไม่ถูกต้องครับพ่อ!")

    if payload.action_type == "intro_product":
        speech = f"สวัสดีครับพ่อและทุกคน! ร้าน {client.name} ขอเสนอ '{payload.product_name}' {payload.custom_message}"
        color = 0xf59e0b
    elif payload.action_type == "pitch_features":
        speech = f"จุดเด่น '{payload.product_name}' คือ {payload.custom_message} สั่งซื้อกันได้เลยครับ!"
        color = 0xef4444
    elif payload.action_type == "order_alert":
        speech = f"🎉 ขอบคุณคุณ {payload.target_customer} มากครับที่กดสั่งซื้อ '{payload.product_name}' จำนวน {payload.custom_message} จัดส่งด่วนทันทีครับ!"
        color = 0x10b981
    else:
        speech = payload.custom_message or f"กำลังสตรีมสดสินค้า {payload.product_name}"
        color = 0x38bdf8

    broadcast_data = {
        "event": "RENDER_FRAME",
        "speech": speech,
        "color": color,
        "product": payload.product_name
    }

    if connected_clients:
        for ws in list(connected_clients):
            try:
                await ws.send_text(json.dumps(broadcast_data, ensure_ascii=False))
            except:
                connected_clients.remove(ws)

    return {"status": "success", "data": broadcast_data}

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    try:
        with open("../frontend/public/index.html", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "<h1>CO-Live Backend Running Successfully</h1><p>กรุณาตรวจสอบไฟล์ frontend/public/index.html ครับพ่อ</p>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
