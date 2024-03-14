from .SentenceTokenizer import SentenceTokenizer
from nltk import data


class SentenceTokenizerNltk(SentenceTokenizer):
    def __init__(self):
        self.tokenizer = data.load('tokenizers/punkt/spanish.pickle')

    def tokenize_text_by_sentence(self, text: str) -> list:
        tokenized_text = self.tokenizer.tokenize(text)
        return tokenized_text
