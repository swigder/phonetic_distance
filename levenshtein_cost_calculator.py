class LevenshteinCostCalculator:
    def insertion_cost(self, letter):
        return 1

    def deletion_cost(self, letter):
        return 1

    def substitution_cost(self, letter1, letter2):
        return 0 if letter1 == letter2 else 2
