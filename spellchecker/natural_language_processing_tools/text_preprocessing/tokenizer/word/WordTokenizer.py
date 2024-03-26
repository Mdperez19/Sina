from abc import ABCMeta, abstractmethod


class WordTokenizer(metaclass=ABCMeta):
    @abstractmethod
    def tokenize_sentence_by_words(self, sentence: list) -> list:
        pass
