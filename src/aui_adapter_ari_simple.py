
class AriAdapter:
    def __init__(self) -> None:
        self.push_digit = lambda ch: None  # core setzt diese Funktion
    def speak(self, text: str) -> None: print(f"[ARI] speak: {text}")
    def stop_speak(self) -> None: print("[ARI] stop_speak")
    def play(self, uri: str) -> None: print(f"[ARI] play: {uri}")
    def stop_play(self) -> None: print("[ARI] stop_play")
    def ring(self) -> None: print("[ARI] ring")
    def hangup(self) -> None: print("[ARI] hangup")
