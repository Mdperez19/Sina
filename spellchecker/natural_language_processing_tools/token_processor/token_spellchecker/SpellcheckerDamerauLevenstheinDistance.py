from spellchecker.natural_language_processing_tools.token_processor.damerau_levenshtein_distance.DamerauLevenshteinDistance import \
    DamerauLevenshteinDistance
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker import SearchSpaceEnum
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker.SearchSpaceEnum import \
    SearchSpaceEnum
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker.Spellcheker import Spellchecker
from spellchecker.entity.Dictionary import Dictionary
from spellchecker.response_entities.Correction import Correction
from spellchecker.response_entities.PossibleCorrections import PossibleCorrections
import pymongo


class SpellcheckerDamerauLevensteinDistance(Spellchecker):
    def __init__(self, database: Dictionary, damerau_levenshtein_distance: DamerauLevenshteinDistance):

        self.database = database
        self.damerau_levenshtein_distance = damerau_levenshtein_distance

        self.database.connect_to_database()

    def spellcheck_sentences_tokens(self, normalized_sentences_tokens: list) -> list:
        letters_collection = self.database.get_collection_from_database()
        possible_corrections_for_sentences = []

        correct_words = set()
        wrong_words = set()

        for tokens_by_sentence in normalized_sentences_tokens:
            possible_corrections_by_sentence = []

            for token in tokens_by_sentence:
                if len(token) == 1:
                    continue
                else:
                    if token in correct_words or token in wrong_words:
                        continue

                    search_space = self.get_search_space_for_token(token)
                    possible_corrections_for_token = self.look_for_token_in_database(
                        token,
                        search_space,
                        letters_collection
                    )
                    if possible_corrections_for_token:
                        possible_corrections = PossibleCorrections(token, possible_corrections_for_token).to_dict()
                        if not possible_corrections:
                            correct_words.add(token)
                        else:
                            wrong_words.add(token)
                        possible_corrections_by_sentence.append(possible_corrections)
            possible_corrections_for_sentences.append(possible_corrections_by_sentence)
        return possible_corrections_for_sentences

    def get_search_space_for_token(self, token: str) -> list:
        first_letter_of_token = self.get_first_letter_of_token(token)
        print("Token: ", token, "First letter: ", first_letter_of_token)
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
                                   letters_collection: pymongo.collection) -> list:
        possible_corrections = []
        for letter in search_space:
            document = letters_collection.find_one({'letter': letter})

            if document is None:
                continue

            words = document["words"]

            if token in words:
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
