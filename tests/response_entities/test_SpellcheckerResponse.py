import pytest

from spellchecker.response_entities.SpellcheckerResponse import SpellcheckerResponse


class TestSpellcheckerReponse:

    @pytest.fixture
    def spellchecker_response(self):
        return SpellcheckerResponse("El bosque es un lugar mágico para las princesas",
                                    [
                                        {'token': 'pricesas',
                                         'corrections': [
                                            {'word': 'princesas', 'distance': 0.1},
                                            {'word': 'princesitas', 'distance': 0.2},
                                            {'word': 'pinceles', 'distance': 0.3}
                                        ]}
                                    ])

    @pytest.mark.SpellcheckerResponse
    def test_to_dict(self, spellchecker_response):
        # Given init data
        # When
        result = spellchecker_response.to_dict()
        # Then
        assert isinstance(result, dict)
        assert isinstance(result["original_sentence"],str)
        assert result["possible_corrections"] == [
                                        {'token': 'pricesas',
                                         'corrections': [
                                            {'word': 'princesas', 'distance': 0.1},
                                            {'word': 'princesitas', 'distance': 0.2},
                                            {'word': 'pinceles', 'distance': 0.3}
                                        ]}
                                    ]
        assert isinstance(result["possible_corrections"], list)
