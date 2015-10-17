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
