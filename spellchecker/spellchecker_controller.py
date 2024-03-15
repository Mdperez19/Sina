from flask import Blueprint, jsonify, request, Response

from .entity.Dictionary import Dictionary
from spellchecker.natural_language_processing_tools.text_preprocessing.tokenizer.sentence.SentenceTokenizerNltk import SentenceTokenizerNltk
from spellchecker.natural_language_processing_tools.text_preprocessing.tokenizer.word.WordTokenizerNltk import WordTokenizerNltk
from .natural_language_processing_tools.text_preprocessing.normalizer.NormalizerPython import NormalizerPython
from spellchecker.natural_language_processing_tools.token_processor.damerau_levenshtein_distance.DamerauLevenshteinDistance import DamerauLevenshteinDistance
from spellchecker.natural_language_processing_tools.token_processor.token_spellchecker.SpellcheckerDamerauLevenstheinDistance import SpellcheckerDamerauLevensteinDistance
from .spellchecker_service import SpellcheckerService
from http import HTTPStatus

spellchecker_api = Blueprint('spellchecker_api', __name__)

sentence_tokenizer = SentenceTokenizerNltk()
word_tokenizer = WordTokenizerNltk()
normalizer = NormalizerPython()
dictionary = Dictionary()
damerau_levenshtein_distance = DamerauLevenshteinDistance()
spellchecker = SpellcheckerDamerauLevensteinDistance(dictionary, damerau_levenshtein_distance)


@spellchecker_api.route('/', methods=['POST'])
def spellcheck() -> tuple[Response, int]:
    if request.is_json:
        data = request.get_json()
        text = data.get('text')
        if text:
            service = SpellcheckerService(sentence_tokenizer, word_tokenizer, normalizer, spellchecker)
            result = service.spellcheck(text)
            return jsonify(result), HTTPStatus.OK
        else:
            return jsonify(
                {'error': 'The "text" field is required on the body of the request'}), HTTPStatus.BAD_REQUEST
    else:
        return jsonify({'error': 'The request must be on JSON format'}), HTTPStatus.BAD_REQUEST
