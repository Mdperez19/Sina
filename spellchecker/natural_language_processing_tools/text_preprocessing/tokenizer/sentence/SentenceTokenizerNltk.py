from .SentenceTokenizer import SentenceTokenizer
from nltk import data
import nltk


class SentenceTokenizerNltk(SentenceTokenizer):
    def __init__(self):
        nltk.download('punkt')
        self.tokenizer = data.load('tokenizers/punkt/spanish.pickle')

    def tokenize_text_by_sentence(self, text: str) -> list:
        tokenized_text = self.tokenizer.tokenize(text)
        return tokenized_text
