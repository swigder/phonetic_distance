import sys
from minimum_edit_distance import minimum_edit_distance
from cmu_dict_phonetic_dictionary import get_pronunciation
from phonetic_cost_calculator import PhoneticCostCalculator


def minimum_phonetic_distance(target, source):
    target_pronunciations = get_pronunciation(target)
    source_pronunciations = get_pronunciation(source)

    minimum_distance = sys.maxsize
    phonetic_calculator = PhoneticCostCalculator()

    for source_pronunciation in source_pronunciations:
        for target_pronunciation in target_pronunciations:
            distance = minimum_edit_distance(target_pronunciation, source_pronunciation, phonetic_calculator)
            if distance < minimum_distance:
                minimum_distance = distance
    return minimum_distance


def closest_word(target, sources):
    minimum_distance = sys.maxsize
    closest = ''

    for source in sources:
        distance = minimum_phonetic_distance(target, source)
        print(source, distance)
        if distance < minimum_distance:
            minimum_distance = distance
            closest = source

    return closest

if __name__ == '__main__':
    minimum_phonetic_distance("KRYPTON", "ABDICATE")
