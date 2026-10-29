class MusicService:
    def __init__(self):
        self.playlist = ["soft-piano", "uplift-loop", "ambient-echo"]

    def generate_bgm(self, cue: str) -> dict:
        return {"cue": cue, "track": self.playlist[0], "status": "ready"}
