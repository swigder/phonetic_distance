from nltk.corpus import cmudict


class CmuDictPhoneticDictionary:
    """
    Facade over the CMUDict that stores dictionary in memory to improve performance.
    """

    dictionary = cmudict.dict()

    def get_pronunciation(self, word):
        """
        Gets the pronunciation from CMUDict, stripping stress information
        :param word: word for which to look up pronunciation; capitalization-agnostic
        :return: list of lists, where each list is one pronunciation, and each item in the list is an ARPAbet phone
        """
        pronunciations = self.dictionary[word.lower()]
        return [[phone[0:-1] if phone.endswith(('0', '1', '2')) else phone for phone in pronunciation] for pronunciation in pronunciations]
