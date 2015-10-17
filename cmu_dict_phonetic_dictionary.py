from nltk.corpus import cmudict


def get_pronunciation(word):
    """
    Gets the pronunciation from CMUDict, stripping stress information
    :param word: word for which to look up pronunciation; capitalization-agnostic
    :return: list of lists, where each list is one pronunciation, and each item in the list is an ARPAbet phone
    """
    pronunciations = cmudict.dict()[word.lower()]
    return [[phone[0:-1] if phone.endswith(('0', '1', '2')) else phone for phone in pronunciation] for pronunciation in pronunciations]
