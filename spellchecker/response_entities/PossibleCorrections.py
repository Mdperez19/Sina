from .Correction import Correction
from typing import List


class PossibleCorrections:
    corrections: List[Correction]
    token: str

    def __init__(self, token: str, corrections: List[Correction]) -> None:
        self.token = token
        self.corrections = corrections

    def to_dict(self) -> dict:
        corrections_sorted = [correction for correction in sorted(self.corrections, reverse=True, key=lambda x: x["distance"])]
        return {
            "token": self.token,
            "corrections": corrections_sorted[:5] if len(corrections_sorted) > 5 else corrections_sorted
        }
