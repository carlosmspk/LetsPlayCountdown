from tqdm import tqdm
from itertools import permutations


def next_step(dictionary, operation_string, numbers, order):
    if order > 5:
        return

    this_operation_string = operation_string + " + " + str(numbers[order])
    dictionary[this_operation_string] = dictionary[operation_string] + numbers[order]
    next_step(dictionary, this_operation_string, numbers, order + 1)

    this_operation_string = operation_string + " - " + str(numbers[order])
    dictionary[this_operation_string] = dictionary[operation_string] - numbers[order]
    next_step(dictionary, this_operation_string, numbers, order + 1)

    this_operation_string = operation_string + " x " + str(numbers[order])
    dictionary[this_operation_string] = dictionary[operation_string] * numbers[order]
    next_step(dictionary, this_operation_string, numbers, order + 1)

    if dictionary[operation_string] % numbers[order] == 0:
        this_operation_string = operation_string + " / " + str(numbers[order])
        dictionary[this_operation_string] = (
            dictionary[operation_string] // numbers[order]
        )
        next_step(dictionary, this_operation_string, numbers, order + 1)


def check_arithmetic_combos(dictionary, number_order: tuple):

    accumulator = number_order[0]
    operation_string = str(number_order[0])

    dictionary[operation_string] = accumulator
    next_step(dictionary, operation_string, number_order, 1)


def get_min_dist(target, dictionary):
    min_distance_to_target = target

    for _, value in dictionary.items():
        if abs(value - target) < min_distance_to_target:
            min_distance_to_target = abs(value - target)
    return min_distance_to_target


def get_best_results(target, dictionary):
    min_distance_to_target = get_min_dist(target, dictionary)

    possibilities = []
    for op, value in dictionary.items():
        if abs(value - target) == min_distance_to_target:
            possibilities.append(op)
    return possibilities, min_distance_to_target


def get_closest_results(numbers, target) -> tuple[int, list, dict]:
    raw_input = [i for i in permutations(numbers)]

    dictionary = {}

    for number_order in raw_input:
        check_arithmetic_combos(dictionary, number_order)

    possibilities, min_distance_to_target = get_best_results(target, dictionary)

    return min_distance_to_target, possibilities, dictionary


def run_numbers():
    print("Insert numbers, one by one, seperated by ENTER:\n")
    numbers = []
    for i in range(6):
        numbers.append(int(input("Number " + str(i + 1) + ": ")))
    target = int(input("And the target is... "))
    distance_to_target, solutions, dictionary = get_closest_results(numbers, target)

    if distance_to_target == 0:
        if len(solutions) > 1:
            print("Found a couple of ways to do it (" + str(len(solutions)) + " ways)...")
            for way, solution in enumerate(solutions, 1):
                print(way,":\t",solution, "=", dictionary[solution])
        else:
            print(solutions[0], "=", dictionary[solutions[0]])
    else:
        print("Didn't quite get there, " + str(distance_to_target) + " away...")
        for way, solution in enumerate(solutions, 1):
            print(way,":\t",solution, "=", dictionary[solution])
