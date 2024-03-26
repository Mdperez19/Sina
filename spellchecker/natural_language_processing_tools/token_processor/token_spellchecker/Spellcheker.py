from abc import ABCMeta, abstractmethod


class Spellchecker(metaclass=ABCMeta):
    @abstractmethod
    def spellcheck_sentences_tokens(self, normalized_sentences_tokens: list) -> list:
        pass
