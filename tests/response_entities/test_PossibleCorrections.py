import pytest

from spellchecker.response_entities.PossibleCorrections import PossibleCorrections


class TestPossibleCorrections:

    @pytest.fixture
    def possible_corrections(self):
        return PossibleCorrections("pricesa",
                                   [
                                       {'word': 'princesa', 'distance': 0.875},
                                       {'word': 'princesita', 'distance': 0.5}
                                   ])

    @pytest.mark.PossibleCorrections
    def test_to_dict(self, possible_corrections):
        # Given init data
        # When
        result = possible_corrections.to_dict()
        # Then
        assert isinstance(result, dict)
        assert result["token"] == "pricesa"
        assert result["corrections"] == [
                                       {'word': 'princesa', 'distance': 0.875},
                                       {'word': 'princesita', 'distance': 0.5}
                                   ]
        assert isinstance(result["corrections"], list)
