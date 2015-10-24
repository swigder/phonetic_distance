from phonetic_distance.minimum_edit_distance import minimum_edit_distance
from phonetic_distance.levenshtein_cost_calculator import LevenshteinCostCalculator


class TestMinimumEditDistance:

    def test_minimum_edit_distance(self):
        assert minimum_edit_distance("intention", "execution", LevenshteinCostCalculator()) == 8
        assert minimum_edit_distance("drive", "brief", LevenshteinCostCalculator()) == 4
        assert minimum_edit_distance("drive", "divers", LevenshteinCostCalculator()) == 3

