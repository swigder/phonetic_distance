import argparse

from nltk.corpus import cmudict

from phonetic_distance.minimum_phonetic_distance_calculator import MinimumPhoneticDistanceCalculator
from phonetic_distance.cmu_dict_phonetic_dictionary import CmuDictPhoneticDictionary
from phonetic_distance.phonetic_cost_calculator import PhoneticCostCalculator
from phonetic_distance.utilities import binary_search

cmu_dictionary = CmuDictPhoneticDictionary()


def minimum_phonetic_distance(target, source, similar_phone_substitution_cost, **kwargs):
    phonetic_cost_calculator = PhoneticCostCalculator(similar_phone_substitution_cost)
    calculator = MinimumPhoneticDistanceCalculator(cmu_dictionary, phonetic_cost_calculator)

    return calculator.minimum_phonetic_distance(target, source)


def closest_word(target, sources, similar_phone_substitution_cost):
    phonetic_cost_calculator = PhoneticCostCalculator(similar_phone_substitution_cost)
    calculator = MinimumPhoneticDistanceCalculator(cmu_dictionary, phonetic_cost_calculator)

    return calculator.closest_words(target, sources)


def closest_word_for_letter(target, first_letter, similar_phone_substitution_cost):
    first_letter = first_letter.lower()
    words = cmudict.words()
    letter_start = binary_search(words, first_letter, lambda x, y: 0 if x == y else 1 if x > y else -1)
    letter_end = binary_search(words, chr(ord(first_letter) + 1), lambda x, y: 0 if x == y else 1 if x > y else -1)
    return closest_word(target, words[letter_start:letter_end], similar_phone_substitution_cost)


def closest_word_wrapper(target, sources, first_letter, similar_phone_substitution_cost, **kwargs):
    if first_letter:
        return closest_word_for_letter(target, first_letter, similar_phone_substitution_cost)
    else:
        return closest_word(target, sources, similar_phone_substitution_cost)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Minimum Phonetic Dictionary.')

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_minimum_phonetic_distance = subparsers.add_parser('minimum_phonetic_distance',
                                                             help='minimum_phonetic_distance help')
    parser_minimum_phonetic_distance.add_argument('target', type=str, help='target word')
    parser_minimum_phonetic_distance.add_argument('source', type=str, help='source word')
    parser_minimum_phonetic_distance.set_defaults(func=minimum_phonetic_distance)

    parser_closest_word = subparsers.add_parser('closest_word', help='closest_word help')
    parser_closest_word.add_argument('target', type=str, help='target word')
    parser_closest_word.add_argument('sources', type=str, nargs='*', help='source words')
    parser_closest_word.add_argument('-fl', '--first_letter', type=str, nargs='?')
    parser_closest_word.set_defaults(func=closest_word_wrapper)

    parser.add_argument('-sc', '--similar_phone_substitution_cost', type=float, default=1,
                        help='cost for a substituting similar phones')

    args = parser.parse_args()
    print(args.func(**vars(args)))
