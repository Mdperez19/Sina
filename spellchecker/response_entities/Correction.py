class Correction:
    distance: int
    word: str

    def __init__(self, word: str, distance: int) -> None:
        self.word = word
        self.distance = distance

    def to_dict(self) -> dict:
        return {
            "word": self.word,
            "distance": self.distance
        }
