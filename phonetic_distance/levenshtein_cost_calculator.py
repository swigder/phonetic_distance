class LevenshteinCostCalculator:
    """
    Cost calculator using Levenshtein minimum edit distance costs of 1 for insertion and deletion and 2 for substitution
    (given a letter is not substituted for itself).
    Can also be used as a basic cost calculator for non-letter inputs.
    """

    def insertion_cost(self, letter):
        """
        Returns cost of inserting a given letter (or other item)
        :param letter: the letter to be inserted
        :return: constant cost of 1 for any letter
        """
        return 1

    def deletion_cost(self, letter):
        """
        Returns cost of deleting a given letter (or other item)
        :param letter: the letter to be deleted
        :return: constant cost of 2 for any letter
        """
        return 1

    def substitution_cost(self, letter1, letter2):
        """
        Returns cost of substituting one letter (or other item) for another
        :param letter1: letter to be substituted
        :param letter2: letter to substitute with
        :return: constant cost of 2 if the letters are different, 0 otherwise (equivalent to an insertion + deletion)
        """
        return 0 if letter1 == letter2 else 2
