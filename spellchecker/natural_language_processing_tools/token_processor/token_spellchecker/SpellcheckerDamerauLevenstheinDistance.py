from spellchecker.natural_language_processing_tools.token_processor.damerau_levenshtein_distance.DamerauLevenshteinDistance import \
    DamerauLevenshteinDistance
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker import SearchSpaceEnum
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker.SearchSpaceEnum import \
    SearchSpaceEnum
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker.Spellchecker import Spellchecker
from spellchecker.entity.Dictionary import Dictionary
from spellchecker.response_entities.Correction import Correction
from spellchecker.response_entities.PossibleCorrections import PossibleCorrections
import bisect
import pymongo


class SpellcheckerDamerauLevensteinDistance(Spellchecker):
    def __init__(self, database: Dictionary, damerau_levenshtein_distance: DamerauLevenshteinDistance):

        self.database = database
        self.damerau_levenshtein_distance = damerau_levenshtein_distance

        self.database.connect_to_database()

    def spellcheck_sentences_tokens(self,
                                    normalized_sentences_tokens: list[list[str]]
                                    ) -> list:
        letters_collection = self.database.get_collection_from_database()
        possible_corrections_for_sentences = self.collect_possible_corrections_by_sentence(
            normalized_sentences_tokens,
            letters_collection
        )
        return possible_corrections_for_sentences

    def collect_possible_corrections_by_sentence(self,
                                                 normalized_sentences_tokens: list[list[str]],
                                                 letters_collection: pymongo.collection
                                                 ) -> list:
        possible_corrections_for_sentences = []
        checked_tokens = set()
        for tokens_by_sentence in normalized_sentences_tokens:
            possible_corrections_by_sentence = self.collect_possible_corrections_for_tokens(tokens_by_sentence,
                                                                                            checked_tokens,
                                                                                            letters_collection)
            possible_corrections_for_sentences.append(possible_corrections_by_sentence)

        return possible_corrections_for_sentences

    def collect_possible_corrections_for_tokens(self, tokens_by_sentence: list[str],
                                                checked_tokens: set,
                                                letters_collection: pymongo.collection
                                                ) -> list:
        possible_corrections_by_sentence = []
        for token in tokens_by_sentence:
            if token in checked_tokens:
                continue

            possible_corrections_for_token = self.collect_possible_corrections_for_token(token, letters_collection)
            if possible_corrections_for_token:
                possible_corrections = PossibleCorrections(token, possible_corrections_for_token).to_dict()
                possible_corrections_by_sentence.append(possible_corrections)

            checked_tokens.add(token)
        return possible_corrections_by_sentence

    def collect_possible_corrections_for_token(self,
                                               token: str,
                                               letters_collection: pymongo.collection
                                               ) -> list:
        search_space = self.get_search_space_for_token(token)
        possible_corrections_for_token = self.look_for_token_in_database(
            token,
            search_space,
            letters_collection
        )
        return possible_corrections_for_token

    def get_search_space_for_token(self, token: str) -> list:
        first_letter_of_token = self.get_first_letter_of_token(token)
        search_space_for_token = SearchSpaceEnum[first_letter_of_token.upper()].value
        return search_space_for_token

    @staticmethod
    def get_first_letter_of_token(token: str) -> str:
        accented_letters = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
        first_letter = token[0]

        if first_letter in accented_letters:
            return f"{accented_letters[first_letter]}_acc"
        else:
            return first_letter

    def look_for_token_in_database(self, token: str, search_space: list,
                                   letters_collection: pymongo.collection) -> list[dict]:
        possible_corrections = []
        for letter in search_space:
            document = letters_collection.find_one({'letter': letter})

            if document is None:
                continue

            words = document["words"]

            index_of_token = bisect.bisect_left(words, token)

            is_index_within_bounds = index_of_token < len(words)

            if is_index_within_bounds and words[index_of_token] == token:
                break
            else:
                for word in words:
                    distance_between_words = (self.damerau_levenshtein_distance
                    .calculate_normalized_levenshtein_distance(
                        token,
                        word
                    )
                    )

                    if distance_between_words != -1:
                        correction = Correction(word, distance_between_words).to_dict()
                        possible_corrections.append(correction)

        return possible_corrections
