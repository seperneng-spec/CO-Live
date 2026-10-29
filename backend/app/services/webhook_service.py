class WebhookService:
    def handle_event(self, payload: dict) -> dict:
        return {"received": True, "payload": payload}
