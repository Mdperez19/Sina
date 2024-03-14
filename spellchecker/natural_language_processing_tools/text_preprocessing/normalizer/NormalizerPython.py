from .Normalizer import Normalizer


class NormalizerPython(Normalizer):
    def __init__(self):
        pass

    def normalize_sentences_tokens(self, sentences_tokens: list) -> list:
        normalized_sentences_tokens = []
        for tokens_by_sentence in sentences_tokens:
            normalized_tokens_by_sentence = []
            for token in tokens_by_sentence:
                if len(token) == 1 and not token.isalnum():
                    continue
                else:
                    normalized_token = self.build_normalized_token(token)
                    normalized_tokens_by_sentence.append(normalized_token)
            normalized_sentences_tokens.append(normalized_tokens_by_sentence)

        return normalized_sentences_tokens

    @staticmethod
    def build_normalized_token(token: str) -> str:
        normalized_token = ''.join(
            character for character in token
            if character.isalpha()
        )

        return normalized_token.lower()
