from abc import ABCMeta, abstractmethod


class Normalizer(metaclass=ABCMeta):
    @abstractmethod
    def normalize_sentences_tokens(self, sentences_tokens: list) -> list:
        pass
