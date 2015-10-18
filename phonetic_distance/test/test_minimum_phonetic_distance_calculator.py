from nltk.corpus import cmudict

from phonetic_distance.minimum_phonetic_distance_calculator import MinimumPhoneticDistanceCalculator
from phonetic_distance.cmu_dict_phonetic_dictionary import CmuDictPhoneticDictionary
from phonetic_distance.phonetic_cost_calculator import PhoneticCostCalculator
from phonetic_distance.utilities import binary_search

class TestMinimumPhoneticDistance:

    calculator = MinimumPhoneticDistanceCalculator(CmuDictPhoneticDictionary(), PhoneticCostCalculator())

    def test_minimum_phonetic_distance(self):
        assert self.calculator.minimum_phonetic_distance("MONETARY", "MONOTONE") == 3.5
        assert self.calculator.minimum_phonetic_distance("MONETARY", "COMMENTARY") == 3.5

    def test_closest_word(self):
        words = cmudict.words()
        c_start = binary_search(words, 'c', lambda x, y: 0 if x == y else 1 if x > y else -1)
        c_end = binary_search(words, 'd', lambda x, y: 0 if x == y else 1 if x > y else -1)
        self.calculator.closest_word("KRYPTON", words[c_start:c_end])
