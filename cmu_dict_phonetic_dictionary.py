import nltk
from nltk.corpus import cmudict


def print_pronunciation():
    cmudict.dict()
    print(cmudict.entries()[653:659])
