from abc import ABCMeta, abstractmethod


class SentenceTokenizer(metaclass=ABCMeta):
    @abstractmethod
    def tokenize_text_by_sentence(self, text: str) -> list:
        pass
