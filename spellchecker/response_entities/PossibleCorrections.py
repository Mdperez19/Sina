from .Correction import Correction
from typing import List


class PossibleCorrections:
    corrections: List[Correction]
    token: str

    def __init__(self, token: str, corrections: List[Correction]) -> None:
        self.token = token
        self.corrections = corrections

    def to_dict(self) -> dict:
        return {
            "token": self.token,
            "corrections": list(self.corrections)
        }
