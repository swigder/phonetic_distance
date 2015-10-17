import pytest
from mock import Mock
from minimum_edit_distance import minimum_edit_distance
from levenshtein_cost_calculator import LevenshteinCostCalculator


class TestMinimumEditDistance:

    def test_minimum_edit_distance(self):
        assert minimum_edit_distance("intention", "execution", LevenshteinCostCalculator()) == 8

