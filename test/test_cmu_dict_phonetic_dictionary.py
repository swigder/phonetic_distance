import pytest
from cmu_dict_phonetic_dictionary import get_pronunciation


class TestCmuDictPhoneticDictionary:

    def test_get_pronunciation(self):
        assert get_pronunciation("monetary") == [['M', 'AA', 'N', 'AH', 'T', 'EH', 'R', 'IY']]

    def test_get_pronunciation_upper(self):
        assert get_pronunciation("MONETARY") == [['M', 'AA', 'N', 'AH', 'T', 'EH', 'R', 'IY']]

