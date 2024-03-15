from .WordTokenizer import WordTokenizer
import nltk
from nltk import word_tokenize


class WordTokenizerNltk(WordTokenizer):
    def __init__(self):
        nltk.download('punkt')

    def tokenize_sentence_by_words(self, sentences: list) -> list:
        sentences_tokens = []
        for sentence in sentences:
            tokens = word_tokenize(sentence)
            sentences_tokens.append(tokens)

        return sentences_tokens
