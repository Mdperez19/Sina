import pytest
import pytest_mock

from spellchecker.entity.Dictionary import Dictionary
from spellchecker.natural_language_processing_tools.text_preprocessing.normalizer.NormalizerPython import \
    NormalizerPython
from spellchecker.natural_language_processing_tools.text_preprocessing.tokenizer.sentence.SentenceTokenizerNltk import \
    SentenceTokenizerNltk
from spellchecker.natural_language_processing_tools.text_preprocessing.tokenizer.word.WordTokenizerNltk import \
    WordTokenizerNltk
from spellchecker.natural_language_processing_tools.token_processor.damerau_levenshtein_distance.DamerauLevenshteinDistance import \
    DamerauLevenshteinDistance
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker.SpellcheckerDamerauLevenstheinDistance import \
    SpellcheckerDamerauLevensteinDistance
from spellchecker.spellchecker_service import SpellcheckerService


class TestSpellcheckerService:

    @pytest.fixture
    def sentence_tokenizer(self):
        return SentenceTokenizerNltk()

    @pytest.fixture
    def word_tokenizer(self):
        return WordTokenizerNltk()

    @pytest.fixture
    def normalizer(self):
        return NormalizerPython()

    @pytest.fixture
    def dictionary(self):
        return Dictionary()

    @pytest.fixture
    def damerau_levenshtein_distance(self):
        return DamerauLevenshteinDistance()

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

    @pytest.fixture
    def spellchecker_service(self,
                             sentence_tokenizer,
                             word_tokenizer,
                             normalizer,
                             spellchecker):
        return SpellcheckerService(sentence_tokenizer,
                                   word_tokenizer,
                                   normalizer,
                                   spellchecker)

    @pytest.mark.SpellcheckerService
    def test_spellcheck(self, spellchecker_service, mocker):
        # Given
        text = "La princeso2. Los niñes"
        mocked_possible_corrections = [
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
        mocked_collect_possible_corrections_for_sentences_tokens = mocker.patch.object(
            spellchecker_service.spellchecker,
            'spellcheck_sentences_tokens',
            return_value=mocked_possible_corrections
        )

        expected_result = [
            {
                'original_sentence': 'La princeso2.',
                'possible_corrections': [
                    {'distance': 0.875, 'word': 'princesa'},
                    {'distance': 0.7, 'word': 'princesita'},
                    {'distance': 0.6666666666666666, 'word': 'principio'},
                    {'distance': 0.625, 'word': 'pincel'},
                    {'distance': 0.625, 'word': 'preciso'}
                ]
            },
            {
                'original_sentence': 'Los niñes',
                'possible_corrections': [
                    {'distance': 0.8, 'word': 'niñas'},
                    {'distance': 0.8, 'word': 'niños'},
                    {'distance': 0.6666666666666666, 'word': 'nieves'},
                    {'distance': 0.6, 'word': 'nigel'},
                    {'distance': 0.6, 'word': 'niña'}
                ]
            }
        ]

        # When
        result = spellchecker_service.spellcheck(text)

        # Then
        assert result == expected_result
        assert mocked_collect_possible_corrections_for_sentences_tokens.call_args_list == [
            mocker.call([['la', 'princeso'], ['los', 'niñes']])
        ]

    @pytest.mark.SpellcheckerService
    def test_preprocess_text(self, spellchecker_service):
        # Given
        text = "La princeso2. Los niñes"
        expected_result = (
            [['la', 'princeso'], ['los', 'niñes']], ['La princeso2.', 'Los niñes']
        )

        # When
        result = spellchecker_service.preprocess_text(text)

        # Then
        assert result == expected_result

    @pytest.mark.SpellcheckerService
    def test_format_result(self, spellchecker_service):
        # Given
        possible_corrections = [
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

        normalized_sentences_tokens = [["la", "princeso"], ["los", "niñes"]]

        expected_result = [
            {
                'original_sentence': ['la', 'princeso'],
                'possible_corrections': [
                    {'word': 'princesa', 'distance': 0.875},
                    {'word': 'princesita', 'distance': 0.7},
                    {'word': 'principio', 'distance': 0.6666666666666666},
                    {'word': 'pincel', 'distance': 0.625},
                    {'word': 'preciso', 'distance': 0.625}
                ]
            },
            {
                'original_sentence': ['los', 'niñes'],
                'possible_corrections': [
                    {'word': 'niñas', 'distance': 0.8},
                    {'word': 'niños', 'distance': 0.8},
                    {'word': 'nieves', 'distance': 0.6666666666666666},
                    {'word': 'nigel', 'distance': 0.6},
                    {'word': 'niña', 'distance': 0.6}]
            }
        ]

        # When
        result = spellchecker_service.format_result(possible_corrections, normalized_sentences_tokens)

        # Then
        assert result == expected_result
