from collections.abc import Iterable


class WebSocketManager:
    def __init__(self):
        self.connections: set = set()

    def connect(self, websocket) -> None:
        self.connections.add(websocket)

    def disconnect(self, websocket) -> None:
        self.connections.discard(websocket)

    async def broadcast(self, message: dict) -> None:
        for connection in list(self.connections):
            await connection.send_json(message)

    async def broadcast_text(self, text: str) -> None:
        await self.broadcast({"type": "text", "message": text})
