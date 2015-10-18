import sys
from minimum_edit_distance import minimum_edit_distance
from phonetic_cost_calculator import PhoneticCostCalculator


class MinimumPhoneticDistanceCalculator:
    """
    Calculator of minimum phonetic distances between words using a given phonetic dictionary, given phonetic cost
    calculator, and the standard minimum edit distance algorithm.
    """

    def __init__(self, phonetic_dictionary, phonetic_cost_calculator):
        """
        :param phonetic_dictionary: dictionary that provides phonetic pronunciation of words in form list of
        pronunciations, where each pronunciation is a list of phones
        :param phonetic_cost_calculator: calculator to determine the insertion, deletion, and substitution cost
        for each phone or pair of phone
        """
        self.phonetic_dictionary = phonetic_dictionary
        self.phonetic_cost_calculator = phonetic_cost_calculator

    def minimum_phonetic_distance(self, target, source):
        """
        Provides the minimum phonetic distance between two words by looking up their pronunciations and comparing them
        using the provided phonetic_cost_calculator.  If a word has multiple pronunciations, the distance to the closest
        pronunciation will be used.
        :param target: source word to compare
        :param source: target word to compare
        :return: distance between the pronunciation of the two words for their closest pronunciations; lower is closer
        """
        target_pronunciations = self.phonetic_dictionary.get_pronunciation(target)
        source_pronunciations = self.phonetic_dictionary.get_pronunciation(source)

        minimum_distance = sys.maxsize
        phonetic_calculator = PhoneticCostCalculator()

        for source_pronunciation in source_pronunciations:
            for target_pronunciation in target_pronunciations:
                distance = minimum_edit_distance(target_pronunciation, source_pronunciation, phonetic_calculator)
                if distance < minimum_distance:
                    minimum_distance = distance
        return minimum_distance

    def closest_word(self, target, sources):
        """
        Provides the source word that is closest to the target word out of a list of source words.  For each source
        word, the pronunciation closest to the target word will be considered.
        :param target: the word for which to find the closest match
        :param sources: a list of candidate words from which to find the closest match
        :return: word of sources with a pronunciation closest to target
        """
        minimum_distance = sys.maxsize
        closest = ''

        for source in sources:
            distance = self.minimum_phonetic_distance(target, source)
            print(source, distance)
            if distance < minimum_distance:
                minimum_distance = distance
                closest = source

        return closest
