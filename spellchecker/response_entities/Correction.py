class Correction:
    distance: float
    word: str

    def __init__(self, word: str, distance: float) -> None:
        self.word = word
        self.distance = distance

    def to_dict(self) -> dict:
        return {
            "word": self.word,
            "distance": self.distance
        }
