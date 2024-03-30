import pytest

from spellchecker.response_entities.Correction import Correction


class TestCorrection:

    @pytest.fixture
    def correction(self):
        return Correction("princesa", 0.875)

    @pytest.mark.Correction
    def test_to_dict(self, correction):
        # Given init data
        # When
        result = correction.to_dict()
        print(result)
        # Then
        assert isinstance(result, dict)
        assert result["word"]=="princesa"
        assert result["distance"]==0.875
