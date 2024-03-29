import pytest

from spellchecker.natural_language_processing_tools.text_preprocessing.tokenizer.word.WordTokenizerNltk import \
    WordTokenizerNltk


class TestWordTokenizerNlkt:

    @pytest.fixture
    def word_tokenizer(self):
        return WordTokenizerNltk()

    @pytest.mark.WordTokenizerNlkt
    def test_tokenize_sentence_by_words(self, word_tokenizer):
        sentence = ["Esto es una oración de prueba que debe mostrar 10 tokens",
                    "Esta es otra oración que tendrá 8 tokens"]
        tokens = word_tokenizer.tokenize_sentence_by_words(sentence)
        assert len(tokens) == 2
        assert isinstance(tokens, list)
