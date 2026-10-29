class TTSService:
    def __init__(self):
        self.voice = "thai-female-1"

    def speak(self, text: str) -> dict:
        return {"voice": self.voice, "text": text, "status": "queued"}
