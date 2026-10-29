class SequencerState:
    def __init__(self):
        self.current_index = 0
        self.mood = "neutral"
        self.pose = "idle"
        self.script = []

    def set_script(self, script: list[str]) -> None:
        self.script = script
        self.current_index = 0

    def next(self) -> str | None:
        if not self.script:
            return None
        if self.current_index >= len(self.script):
            self.current_index = 0
        value = self.script[self.current_index]
        self.current_index += 1
        return value

    def set_mood(self, mood: str) -> None:
        self.mood = mood

    def set_pose(self, pose: str) -> None:
        self.pose = pose
