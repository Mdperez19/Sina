import pytest
import pytest_mock
from dotenv import load_dotenv

from spellchecker.entity.Dictionary import Dictionary
from spellchecker.natural_language_processing_tools.token_processor.damerau_levenshtein_distance.DamerauLevenshteinDistance import \
    DamerauLevenshteinDistance
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker.SpellcheckerDamerauLevenstheinDistance import \
    SpellcheckerDamerauLevensteinDistance


class TestSpellcheckerDamerauLevensteinDistance:

    @pytest.fixture(autouse=True)
    def load_env_variables(self):
        load_dotenv()
    @pytest.fixture
    def spellchecker(self, mocker):
        dictionary = Dictionary()
        mocker.patch.object(
            dictionary,
            'connect_to_database',
            return_value=True
        )
        damerauLevenshtein = DamerauLevenshteinDistance()
        return SpellcheckerDamerauLevensteinDistance(dictionary, damerauLevenshtein)


    @pytest.mark.SpellcheckerDamerauLevensteinDistance
    def test_search_space_for_token(self, spellchecker):
        # Given
        token="princesa"
        expected_search_space=['p', 'q', 'b', 'd', 'o', 'l', 'ñ', 'á', 'é', 'í', 'ó', 'ú']
        # When
        result = spellchecker.get_search_space_for_token(token)
        assert result == expected_search_space



    @pytest.mark.SpellcheckerDamerauLevensteinDistance
    def test_get_first_letter_of_token(self, spellchecker):
        # Given
        token = "princesa"
        # When
        result = spellchecker.get_first_letter_of_token(token)
        assert result == "p"
        # Given
        token = "árbol"
        # # When
        result = spellchecker.get_first_letter_of_token(token)
        assert result == "a_acc"
