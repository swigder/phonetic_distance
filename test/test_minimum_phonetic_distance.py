import pytest
from minimum_phonetic_distance import minimum_phonetic_distance


class TestMinimumPhoneticDistance:

    def test_minimum_phonetic_distance(self):
        assert minimum_phonetic_distance("MONETARY", "MONOTONE") == 2
        assert minimum_phonetic_distance("MONETARY", "COMMENTARY") == 4