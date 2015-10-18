from phonetic_distance.cmu_dict_phonetic_dictionary import CmuDictPhoneticDictionary


class TestCmuDictPhoneticDictionary:

    dictionary = CmuDictPhoneticDictionary()

    def test_get_pronunciation(self):
        assert self.dictionary.get_pronunciation("monetary") == [['M', 'AA', 'N', 'AH', 'T', 'EH', 'R', 'IY']]

    def test_get_pronunciation_upper(self):
        assert self.dictionary.get_pronunciation("MONETARY") == [['M', 'AA', 'N', 'AH', 'T', 'EH', 'R', 'IY']]

