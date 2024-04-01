from spellchecker.natural_language_processing_tools.text_preprocessing.tokenizer.sentence.SentenceTokenizer import \
    SentenceTokenizer
from spellchecker.natural_language_processing_tools.text_preprocessing.tokenizer.word.WordTokenizer import WordTokenizer
from spellchecker.natural_language_processing_tools.text_preprocessing.normalizer.Normalizer import Normalizer
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker.Spellchecker import Spellchecker
from spellchecker.response_entities.SpellcheckerResponse import SpellcheckerResponse


class SpellcheckerService:
    def __init__(self, sentence_tokenizer: SentenceTokenizer, word_tokenizer: WordTokenizer, normalizer: Normalizer,
                 spellchecker: Spellchecker):
        self.sentence_tokenizer = sentence_tokenizer
        self.word_tokenizer = word_tokenizer
        self.normalizer = normalizer
        self.spellchecker = spellchecker

    def spellcheck(self, text: str) -> list:
        normalized_sentences_tokens, tokenized_sentences = self.preprocess_text(text)
        possible_corrections = self.spellchecker.spellcheck_sentences_tokens(normalized_sentences_tokens)
        spell_checker_results = self.format_result(possible_corrections, tokenized_sentences)

        return spell_checker_results

    def preprocess_text(self, text: str) -> tuple[list, list]:
        tokenized_sentences = self.sentence_tokenizer.tokenize_text_by_sentence(text)
        sentences_tokens = self.word_tokenizer.tokenize_sentence_by_words(tokenized_sentences)
        normalized_sentences_tokens = self.normalizer.normalize_sentences_tokens(sentences_tokens)

        return normalized_sentences_tokens, tokenized_sentences

    @staticmethod
    def format_result(possible_corrections: list, tokenized_sentences: list) -> list:
        formatted_results = [SpellcheckerResponse(original_sentence, corrections).to_dict() for
                             original_sentence, corrections in zip(tokenized_sentences, possible_corrections) if
                             corrections]

        return formatted_results
