import pytest
from minimum_phonetic_distance import minimum_phonetic_distance
from cmu_dict_phonetic_dictionary import get_pronunciation


class TestMinimumPhoneticDistance:

    def test_minimum_phonetic_distance(self):
        assert minimum_phonetic_distance("MONETARY", "MONOTONE") == 4
        assert minimum_phonetic_distance("MONETARY", "COMMENTARY") == 4
