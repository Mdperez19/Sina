import pytest

from spellchecker.natural_language_processing_tools.token_processor.damerau_levenshtein_distance.DamerauLevenshteinDistance import \
    DamerauLevenshteinDistance


class TestDamerauLevenshteinDistance:

    @pytest.fixture
    def damerau_levenshtein_distance(self):
        return DamerauLevenshteinDistance()

    words_to_test = [
        "papel",
        "princesa",
        "principe",
        "propuesta",
    ]

    @pytest.mark.DamerauLevenshteinDistance
    def test_calculate_distance_between_words(self, damerau_levenshtein_distance):
        # Given
        word_1 = "papel"
        word_2 = "papal"
        expected_result = 1
        # When
        result = damerau_levenshtein_distance.calculate_distance_between_words(word_1, word_2)
        # Then
        assert isinstance(result, int) or isinstance(result, float)
        assert result == expected_result

    @pytest.mark.DamerauLevenshteinDistance
    @pytest.mark.parametrize("word", words_to_test)
    def test_calculate_normalized_levenshtein_distance(self, damerau_levenshtein_distance, word):
        # Given
        word_to_compare = "princesa"
        # When
        result = damerau_levenshtein_distance.calculate_normalized_levenshtein_distance(word, word_to_compare)
        # Then
        assert isinstance(result, int) or isinstance(result, float)

    @pytest.mark.DamerauLevenshteinDistance
    def test_calculate_distance_between_words(self, damerau_levenshtein_distance):
        # Given
        word = "princesa"
        word_to_compare = "princeso"
        expected_result = 1
        # When
        result = damerau_levenshtein_distance.calculate_distance_between_words(word, word_to_compare)
        # Then
        assert isinstance(result, int)
        assert result == expected_result

    @pytest.mark.DamerauLevenshteinDistance
    @pytest.mark.parametrize("word", words_to_test)
    def test_calculate_distance_between_words(self, damerau_levenshtein_distance, word):
        # Given
        word_to_compare = "princesa"
        # When
        result = damerau_levenshtein_distance.calculate_distance_between_words(word, word_to_compare)
        # Then
        assert isinstance(result, int)
        assert result >= 0.0
