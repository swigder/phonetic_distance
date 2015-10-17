import numpy


def minimum_edit_distance(target, source, cost_calculator):
    """
    Calculates the minimum edit distance for two strings or lists
    :param target: object to be
    :param source:
    :param cost_calculator:
    :return: minimum edit distance between source and target, using costs as determined by cost_calculator
    """
    len_target = len(target)
    len_source = len(source)

    distance_matrix = numpy.zeros((len_target + 1, len_source + 1))

    distance_matrix[0][0] = 0

    for i in range(1, len_target + 1):
        distance_matrix[i][0] = distance_matrix[i-1][0] + cost_calculator.insertion_cost(target[i-1])

    for j in range(1, len_source):
        distance_matrix[0][j] = distance_matrix[0][j-1] + cost_calculator.deletion_cost(source[j-1])

    for i in range(1, len_target + 1):
        for j in range(1, len_source + 1):
            insertion_cost = distance_matrix[i-1][j] + cost_calculator.insertion_cost(target[i-1])
            substitution_cost = distance_matrix[i-1][j-1] + cost_calculator.substitution_cost(source[j-1], target[i-1])
            deletion_cost = distance_matrix[i][j-1] + cost_calculator.deletion_cost(source[j-1])
            distance_matrix[i][j] = min(insertion_cost, substitution_cost, deletion_cost)

    print()
    print(distance_matrix)

    return distance_matrix[len_target][len_source]
