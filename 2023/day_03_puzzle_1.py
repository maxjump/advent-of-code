"""Advent of code, 03.12.2023, puzzle 1"""

import os
from typing import Iterable

import numpy as np
from input_handling import read_input_file

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


def generate_integer_and_symbol_arrays(input_array: np.array) -> (np.array, np.array):
    """Generate two arrays, one for integers and one for symbols."""
    integer_array = input_array.copy()
    np.place(integer_array, integer_array < 0, np.nan)
    symbol_array = input_array.copy()
    np.place(symbol_array, symbol_array > 0, np.nan)
    np.place(symbol_array, symbol_array == -1, 1)
    return integer_array, symbol_array


def main(input_array: np.array):
    """TODO"""
    integer_array, symbol_array = generate_integer_and_symbol_arrays(input_array)
    integer_coordinates = []
    integers_found = []
    for line_number, array in enumerate(integer_array):
        # get coordinates of integers
        number_fields = []
        for field_number, field in enumerate(array):
            if all((not np.isnan(field), field >= 0)):
                number_fields.append(field_number)
        # skip if no numbers are found
        if not number_fields:
            continue
        # get coordinates of numbers
        locations_found = []
        current_location = 0
        number_as_string = ""
        for i, number in enumerate(number_fields):
            if i == 0:
                number_as_string = str(int(array[number]))
                locations_found = [[number]]
            elif number == current_location + 1:  # adjacent
                number_as_string += str(int(array[number]))
                locations_found[-1].append(number)
            elif number > current_location + 1:  # not adjacent
                integers_found.append(int(number_as_string))
                locations_found.append([number])
                number_as_string = str(int(array[number]))
            current_location = number
        integers_found.append(int(number_as_string))
        integer_coordinates.append([line_number, locations_found])
    # check whether symbol adjacent
    adjacent_symbol_check = []
    for coordinates in integer_coordinates:
        line, row_list = coordinates
        for rows in row_list:
            lines_to_search = range(
                max(line - 1, 0), min(line + 2, integer_array.shape[0])
            )
            rows_to_search = range(
                max(rows[0] - 1, 0), min(rows[-1] + 2, integer_array.shape[0])
            )
            adjacent_symbol_check.append(
                symbol_at_integer_location(
                    symbol_array, lines_to_search, rows_to_search, line, rows
                )
            )
    relevant_integers = get_relevant_integers(integers_found, adjacent_symbol_check)
    # assert relevant_integers == example_output
    return sum(relevant_integers)


def symbol_at_integer_location(
    symbol_array: np.array,
    lines_to_search: Iterable,
    rows_to_search: Iterable,
    line_of_integer: int,
    rows_of_integer: list[int],
) -> bool:
    """Check whether a symbol is present next to the integer."""
    for line in lines_to_search:
        for row in rows_to_search:
            if symbol_array[line, row] == 1.0:
                return True
    return False


def get_relevant_integers(
    integers_list: list[int], symbols_check: list[bool]
) -> list[int]:
    """Return list of integers which are adjacent to a symbol."""
    clean_list = []
    for i, check in zip(integers_list, symbols_check):
        clean_list.append(i) if check else None
    return clean_list


if __name__ == "__main__":
    puzzle_input = read_input_file(input_file)
    output = determine_input_types(puzzle_input)
    # output = determine_input_types(example_input)
    solution = main(output)
    print(solution)
