"""Advent of code, 01.12.2023, puzzle 1"""

import os
import re

from input_handling import read_input_file

example_input = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]
example_output = [12, 38, 15, 77]
input_file = os.path.join("2023", "input", "day_01_input.txt")

regex_pattern = "[0-9]"


def find_integers_in_string(input_string: str, pattern: str) -> list:
    """Find all integers in a string."""
    return re.findall(pattern=pattern, string=input_string)


def decode_string(list_of_integers: list) -> int:
    """Decode a string to return the first and last number contained as one integer."""
    return int(str(list_of_integers[0]) + str(list_of_integers[-1]))


def sum_decoded_integers(list_of_decoded_integers: list) -> int:
    """Sum all integers in a list."""
    return sum(list_of_decoded_integers)


def validate_example(pattern: str = regex_pattern) -> None:
    """Validate that the processed example input matches the expected output."""
    list_of_decoded_integers = []
    for input_string, expected_integer in zip(example_input, example_output):
        list_of_decoded_integers.append(
            (decode_string(find_integers_in_string(input_string, pattern)))
        )
        assert list_of_decoded_integers[-1] == expected_integer
    assert sum_decoded_integers(list_of_decoded_integers) == sum(example_output)


def solve_puzzle(pattern: str = regex_pattern) -> int:
    """Solve the puzzle."""
    list_of_decoded_integers = []
    puzzle_input = read_input_file(input_file)
    for line in puzzle_input:
        list_of_decoded_integers.append(
            (decode_string(find_integers_in_string(line, pattern)))
        )
    return sum_decoded_integers(list_of_decoded_integers)


if __name__ == "__main__":
    validate_example()
    solution = solve_puzzle()
    print(f"The solution to the puzzle is {solution}.")
