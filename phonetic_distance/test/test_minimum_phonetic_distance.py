from nltk.corpus import cmudict

from phonetic_distance.minimum_phonetic_distance_calculator import MinimumPhoneticDistanceCalculator
from cmu_dict_phonetic_dictionary import CmuDictPhoneticDictionary
from phonetic_cost_calculator import PhoneticCostCalculator


class TestMinimumPhoneticDistance:

    calculator = MinimumPhoneticDistanceCalculator(CmuDictPhoneticDictionary(), PhoneticCostCalculator())

    def test_minimum_phonetic_distance(self):
        assert self.calculator.minimum_phonetic_distance("MONETARY", "MONOTONE") == 4
        assert self.calculator.minimum_phonetic_distance("MONETARY", "COMMENTARY") == 4

    def test_closest_word(self):
        self.calculator.closest_word("KRYPTON", map(lambda x: x[0], cmudict.entries()[0:100]))
