import pytest

from spellchecker.natural_language_processing_tools.text_preprocessing.tokenizer.sentence.SentenceTokenizerNltk import \
    SentenceTokenizerNltk

class TestSentenceTokenizerNlkt:

    @pytest.fixture
    def sentence_tokenizer(self):
        return SentenceTokenizerNltk()

    @pytest.mark.SentenceTokenizerNlkt
    def test_tokenize_text_by_sentence(self, sentence_tokenizer):
        #Given
        text = "Esto es una oración de prueba. Esta es otra oración de prueba."
        expected_tokens = ["Esto es una oración de prueba.", "Esta es otra oración de prueba."]
        #When
        tokens = sentence_tokenizer.tokenize_text_by_sentence(text)
        #Then
        assert len(tokens) == 2
        assert isinstance(tokens, list)
        assert tokens == expected_tokens
