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
            return_value=True,

        )
        damerau_levenshtein = DamerauLevenshteinDistance()
        return SpellcheckerDamerauLevensteinDistance(dictionary, damerau_levenshtein)

    @pytest.mark.SpellcheckerDamerauLevensteinDistance
    def test_spellcheck_sentences_tokens(self, spellchecker, mocker):
        # Given
        normalized_sentences_tokens = [["la", "princeso"], ["los", "niñes"]]
        possible_corrections_by_token = [
            [
                {'word': 'princesa', 'distance': 0.875},
                {'word': 'princesita', 'distance': 0.7},
                {'word': 'principio', 'distance': 0.6666666666666666},
                {'word': 'pincel', 'distance': 0.625},
                {'word': 'preciso', 'distance': 0.625}
            ],
            [
                {'word': 'niñas', 'distance': 0.8},
                {'word': 'niños', 'distance': 0.8},
                {'word': 'nieves', 'distance': 0.6666666666666666},
                {'word': 'nigel', 'distance': 0.6},
                {'word': 'niña', 'distance': 0.6}
            ]
        ]
        expected_result = [
            [
                {'distance': 0.875, 'word': 'princesa'},
                {'distance': 0.7, 'word': 'princesita'},
                {'distance': 0.6666666666666666, 'word': 'principio'},
                {'distance': 0.625, 'word': 'pincel'},
                {'distance': 0.625, 'word': 'preciso'}],
            [
                {'distance': 0.8, 'word': 'niñas'},
                {'distance': 0.8, 'word': 'niños'},
                {'distance': 0.6666666666666666, 'word': 'nieves'},
                {'distance': 0.6, 'word': 'nigel'},
                {'distance': 0.6, 'word': 'niña'}
            ]
        ]
        mocked_collect_possible_corrections_by_sentence = mocker.patch.object(
            spellchecker,
            'collect_possible_corrections_by_sentence',
            return_value=expected_result
        )
        # When
        result = spellchecker.spellcheck_sentences_tokens(normalized_sentences_tokens)
        # Then
        assert result == expected_result
        assert mocked_collect_possible_corrections_by_sentence.call_count == 1
        assert mocked_collect_possible_corrections_by_sentence.call_args_list == [
            mocker.call(normalized_sentences_tokens, mocker.ANY)
        ]

    @pytest.mark.SpellcheckerDamerauLevensteinDistance
    def test_collect_possible_corrections_by_sentence(self, spellchecker, mocker):
        # Given
        normalized_sentences_tokens = [["la", "princeso"], ["los", "niñes"]]
        possible_corrections_by_token = [
            [
                {'word': 'princesa', 'distance': 0.875},
                {'word': 'princesita', 'distance': 0.7},
                {'word': 'principio', 'distance': 0.6666666666666666},
                {'word': 'pincel', 'distance': 0.625},
                {'word': 'preciso', 'distance': 0.625}
            ],
            [
                {'word': 'niñas', 'distance': 0.8},
                {'word': 'niños', 'distance': 0.8},
                {'word': 'nieves', 'distance': 0.6666666666666666},
                {'word': 'nigel', 'distance': 0.6},
                {'word': 'niña', 'distance': 0.6}
            ]
        ]
        expected_result = [
            [
                {'distance': 0.875, 'word': 'princesa'},
                {'distance': 0.7, 'word': 'princesita'},
                {'distance': 0.6666666666666666, 'word': 'principio'},
                {'distance': 0.625, 'word': 'pincel'},
                {'distance': 0.625, 'word': 'preciso'}],
            [
                {'distance': 0.8, 'word': 'niñas'},
                {'distance': 0.8, 'word': 'niños'},
                {'distance': 0.6666666666666666, 'word': 'nieves'},
                {'distance': 0.6, 'word': 'nigel'},
                {'distance': 0.6, 'word': 'niña'}
            ]
        ]

        mocked_collect_possible_corrections_for_tokens = mocker.patch.object(
            spellchecker,
            'collect_possible_corrections_for_tokens',
            side_effect=possible_corrections_by_token
        )
        letters_collection = mocker.MagicMock()
        # When
        result = spellchecker.collect_possible_corrections_by_sentence(normalized_sentences_tokens,
                                                                       letters_collection)
        # Then
        assert result == expected_result
        assert mocked_collect_possible_corrections_for_tokens.call_count == 2
        assert mocked_collect_possible_corrections_for_tokens.call_args_list == [
            mocker.call(['la', 'princeso'], set(), letters_collection),
            mocker.call(['los', 'niñes'], set(), letters_collection)
        ]

    @pytest.mark.SpellcheckerDamerauLevensteinDistance
    def test_spellcheck_sentences_tokens(self, spellchecker, mocker):
        # Given
        tokens_by_sentence = ["la", "princeso"]

        possible_corrections_by_token = [
            [],
            [{'word': 'peces', 'distance': 0.5},
             {'word': 'peine', 'distance': 0.5},
             {'word': 'perteneces', 'distance': 0.5},
             {'word': 'princesa', 'distance': 0.875},
             {'word': 'princesita', 'distance': 0.7}],

        ]
        expected_result = [{'corrections': [{'distance': 0.875, 'word': 'princesa'},
                                            {'distance': 0.7, 'word': 'princesita'},
                                            {'distance': 0.5, 'word': 'peces'},
                                            {'distance': 0.5, 'word': 'peine'},
                                            {'distance': 0.5, 'word': 'perteneces'}],
                            'token': 'princeso'}]
        mocked_collect_possible_corrections_for_token = mocker.patch.object(
            spellchecker,
            'collect_possible_corrections_for_token',
            side_effect=possible_corrections_by_token
        )
        # When
        result = spellchecker.collect_possible_corrections_for_tokens(tokens_by_sentence,
                                                                      set(),
                                                                      mocker.MagicMock()
                                                                      )
        # Then
        assert result == expected_result
        assert mocked_collect_possible_corrections_for_token.call_count == 2

        # Here we are checking the arguments passed to the mocked_collect_possible_corrections_for_token
        # call_args_list is a list of calls, each call is a tuple of (args, kwargs)
        assert mocked_collect_possible_corrections_for_token.call_args_list == [
            mocker.call('la', mocker.ANY),
            mocker.call('princeso', mocker.ANY)
        ]

    @pytest.mark.SpellcheckerDamerauLevensteinDistance
    def test_collect_possible_corrections_for_token(self, spellchecker, mocker):
        # Given
        token = "princeso"
        mocked_possible_corrections = [
            {'word': 'peces', 'distance': 0.5},
            {'word': 'peine', 'distance': 0.5},
            {'word': 'perteneces', 'distance': 0.5},
            {'word': 'princesa', 'distance': 0.875},
            {'word': 'princesita', 'distance': 0.7},
        ]
        mocked_look_for_token_in_database = mocker.patch.object(
            spellchecker,
            'look_for_token_in_database',
            return_value=mocked_possible_corrections
        )
        letters_collection = mocker.MagicMock()
        # When
        result = spellchecker.collect_possible_corrections_for_token(token, letters_collection)
        # Then
        assert result == mocked_possible_corrections
        assert mocked_look_for_token_in_database.call_count == 1

    @pytest.mark.SpellcheckerDamerauLevensteinDistance
    def test_search_space_for_token(self, spellchecker):
        # Given
        token = "princesa"
        expected_search_space = ['p', 'q', 'b', 'd', 'o', 'l', 'ñ', 'á', 'é', 'í', 'ó', 'ú']
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

    @pytest.mark.SpellcheckerDamerauLevensteinDistance
    def test_look_for_token_in_database(self, spellchecker, mocker):
        # Given
        token = "princeso"
        search_space = ['p', 'q', 'b', 'd']
        expected_result = [
            {'distance': 0.5, 'word': 'peces'},
            {'distance': 0.5, 'word': 'perteneces'},
            {'distance': 0.875, 'word': 'princesa'},
            {'distance': 0.5, 'word': 'peces'},
            {'distance': 0.5, 'word': 'perteneces'},
            {'distance': 0.875, 'word': 'princesa'},
            {'distance': 0.5, 'word': 'peces'},
            {'distance': 0.5, 'word': 'perteneces'},
            {'distance': 0.875, 'word': 'princesa'},
            {'distance': 0.5, 'word': 'peces'},
            {'distance': 0.5, 'word': 'perteneces'},
            {'distance': 0.875, 'word': 'princesa'}
        ]
        mocked_letters_collection = mocker.MagicMock()
        mocked_letters_collection_find_one = mocker.patch.object(
            mocked_letters_collection,
            'find_one',
            return_value={'words': ['peces', 'perteneces', 'princesa']}
        )

        # When
        result = spellchecker.look_for_token_in_database(token, search_space, mocked_letters_collection)

        # Then
        assert result == expected_result
        assert mocked_letters_collection_find_one.call_count == len(search_space)
        assert mocked_letters_collection_find_one.call_args_list == [
            mocker.call({'letter': 'p'}),
            mocker.call({'letter': 'q'}),
            mocker.call({'letter': 'b'}),
            mocker.call({'letter': 'd'}),
        ]
