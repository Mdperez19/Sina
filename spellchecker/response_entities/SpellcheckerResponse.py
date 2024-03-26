from .PossibleCorrections import PossibleCorrections
from typing import List


class SpellcheckerResponse:
    original_sentence: str
    possible_corrections: List[PossibleCorrections]

    def __init__(self, original_sentence: str, possible_corrections: List[PossibleCorrections]) -> None:
        self.original_sentence = original_sentence
        self.possible_corrections = possible_corrections

    def to_dict(self) -> dict:
        return {
            "original_sentence": self.original_sentence,
            "possible_corrections": list(self.possible_corrections)
        }
