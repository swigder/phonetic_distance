import pytest
from minimum_phonetic_distance import minimum_phonetic_distance
from minimum_phonetic_distance import closest_word
from nltk.corpus import cmudict


class TestMinimumPhoneticDistance:

    def test_minimum_phonetic_distance(self):
        assert minimum_phonetic_distance("MONETARY", "MONOTONE") == 4
        assert minimum_phonetic_distance("MONETARY", "COMMENTARY") == 4

    def test_closest_word(self):
        # entries = cmudict.entries()
        # start = -1
        # end = -1
        # curr_start = len(entries) / 2
        # curr_end = len(entries) / 2
        # while start == -1 and end == -1:
        #     letter = entries[curr_start][0][0]
        #     if letter == 'b' and entries[curr_start + 1][0][0] == 'c':
        #         start = curr_start + 1

        closest_word("KRYPTON", map(lambda x: x[0], cmudict.entries()[0:100]))
