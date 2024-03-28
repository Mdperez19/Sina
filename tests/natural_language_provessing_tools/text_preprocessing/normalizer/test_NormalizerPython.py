import pytest

from spellchecker.natural_language_processing_tools.text_preprocessing.normalizer.NormalizerPython import NormalizerPython

class TestNormalizerPython:

    @pytest.fixture
    def normalizer(self):
        return NormalizerPython()

    #TODO: fix this test
    @pytest.mark.NormalizerPython
    def test_normalize_sentences_tokens(self,normalizer):
        #Given
        tokens = ["¿Cómo estás&?","Bien, gracias"]
        expected_normalized_tokens = [["cómo","estás"],["bien","gracias"]]
        #When
        normalized_tokens = normalizer.normalize_sentences_tokens(tokens)
        #Then
        assert normalized_tokens == expected_normalized_tokens
    @pytest.mark.NormalizerPython
    def test_build_normalized_token(self, normalizer):
        #Given
        token="Hola%_)*+áéÍÓú"
        expected_normalized_token="holaáéíóú"
        #When
        normalized_token = normalizer.build_normalized_token(token)
        #Then
        assert normalized_token == expected_normalized_token