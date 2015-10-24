from phonetic_distance.phonetic_cost_calculator import PhoneticCostCalculator


class TestPhoneticCostCalculator:

    similar_substitution_cost = 1
    calculator = PhoneticCostCalculator(similar_substitution_cost)
    phones = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW',
              'ER', 'AXR',
              'P', 'B', 'T', 'D', 'K', 'G',
              'CH', 'ZH',
              'F', 'V', 'TH', 'DH', 'S', 'Z', 'SH', 'ZH', 'HH'
              'M', 'EM', 'N', 'EN', 'NG', 'ENG',
              'L', 'EL', 'R', 'DX', 'NX',
              'Y', 'W', 'Q']

    def test_always_returns_insertion_cost_of_one(self):
        for phone in self.phones:
            assert self.calculator.insertion_cost(phone) == 1

    def test_always_returns_deletion_cost_of_one(self):
        for phone in self.phones:
            assert self.calculator.deletion_cost(phone) == 1

    def test_returns_substitution_cost_of_zero_for_same_phone(self):
        for phone in self.phones:
            assert self.calculator.substitution_cost(phone, phone) == 0

    def test_returns_substitution_cost_of_intermediate_value_for_similar_phones(self):
        assert self.calculator.substitution_cost('AA', 'EH') == self.similar_substitution_cost
        assert self.calculator.substitution_cost('ER', 'AXR') == self.similar_substitution_cost
        assert self.calculator.substitution_cost('T', 'G') == self.similar_substitution_cost
        assert self.calculator.substitution_cost('CH', 'ZH') == self.similar_substitution_cost
        assert self.calculator.substitution_cost('V', 'DH') == self.similar_substitution_cost
        assert self.calculator.substitution_cost('N', 'NG') == self.similar_substitution_cost
        assert self.calculator.substitution_cost('L', 'R') == self.similar_substitution_cost
        assert self.calculator.substitution_cost('W', 'Q') == self.similar_substitution_cost

    def test_returns_substitution_cost_of_two_for_dissimilar_phones(self):
        assert self.calculator.substitution_cost('AH', 'G') == 2
        assert self.calculator.substitution_cost('AXR', 'NG') == 2
        assert self.calculator.substitution_cost('P', 'Q') == 2
        assert self.calculator.substitution_cost('ZH', 'S') == 2
        assert self.calculator.substitution_cost('HH', 'D') == 2
        assert self.calculator.substitution_cost('M', 'AO') == 2
        assert self.calculator.substitution_cost('DX', 'UW') == 2
        assert self.calculator.substitution_cost('Q', 'ZH') == 2
