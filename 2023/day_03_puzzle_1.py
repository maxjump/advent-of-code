"""Advent of code, 03.12.2023, puzzle 1"""

import os

import numpy as np

# from input_handling import read_input_file

example_input = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]
example_output = [467, 35, 633, 617, 592, 755, 664, 598]

input_file = os.path.join("2023", "input", "day_03_input.txt")


def determine_field_type(field: str) -> int:
    """Determine the type of an input 'field'.
    Return the integer, -1 for a symbol and -2 for a dot."""
    try:
        return int(field)
    except ValueError:
        return np.nan if field == "." else -1


def determine_input_types(input_str: list[str]) -> np.array:
    """Determine the type of each field in the input string."""
    input_types_list = []
    for line in input_str:
        input_types_list.append([determine_field_type(field) for field in line])
    return np.array(input_types_list)


def main(input_array: np.array):
    """TODO"""
    for line_number, array in enumerate(input_array):
        print(array)
        # get coordinates of integers
        number_fields = []
        for field_number, field in enumerate(array):
            if all((not np.isnan(field), field >= 0)):
                number_fields.append(field_number)
        print(number_fields)
        # skip if no numbers are found
        if not number_fields:
            continue
        # get coordinates of numbers
        numbers_found = []
        locations_found = []
        current_location = 0
        number_as_string = ""
        for i, number in enumerate(number_fields):
            print(number, current_location)
            if i == 0:
                number_as_string = str(int(array[number]))
                locations_found = [[number]]
            elif number == current_location + 1:  # adjacent
                number_as_string += str(int(array[number]))
                locations_found[-1].append(number)
            elif number > current_location + 1:  # not adjacent
                numbers_found.append(int(number_as_string))
                locations_found.append([number])
                number_as_string = str(int(array[number]))
            current_location = number
        numbers_found.append(int(number_as_string))
        print(locations_found, numbers_found)
        # check whether symbol adjacent


if __name__ == "__main__":
    output = determine_input_types(example_input)
    print(output)
    main(output)
