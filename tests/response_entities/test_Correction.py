import pytest

from spellchecker.response_entities.Correction import Correction


class TestCorrection:

    @pytest.fixture
    def correction(self):
        return Correction("word", 0.5)

    @pytest.mark.Correction
    def test_to_dict(self, correction):
        # Given init data
        # When
        result = correction.to_dict()
        # Then
        assert isinstance(result, dict)
