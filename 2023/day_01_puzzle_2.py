"""Advent of code, 01.12.2023, puzzle 2"""

from day_01_puzzle_1 import find_integers_in_string, decode_string, sum_decoded_integers
from input_handling import read_input_file

valid_string_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

example_input = [
    "two1nine",
    "eightwothree",  # one character can be used for two digits!
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

tricky_characters = [
    "o",  # two-one
    "t",  # eight-two, eight-three
    "e",  # one-eight, three-eight, five-eight, nine-eight
    "n",  # seven-nine
]

example_output = [29, 83, 13, 24, 42, 14, 76]


def find_valid_string_digit(input_string: str) -> str:
    """Find a valid string digit in a string."""
    for valid_string_digit in valid_string_digits.keys():
        if valid_string_digit in input_string:
            return valid_string_digit
    return ""


def reset_string_to_check(string_to_check: str) -> str:
    """Reset the string to check for a valid string digit considering tricky characters."""
    if string_to_check[-1] in tricky_characters:
        return string_to_check[-1]
    else:
        return ""


def find_all_integers(input_string: str) -> str:
    """Generate a string to check for a valid string digit."""
    integers_in_string = ""
    string_to_check = ""
    for character in input_string:
        actual_integer = find_integers_in_string(character)
        if actual_integer != "":
            integers_in_string += actual_integer
            string_to_check = ""
        else:
            string_to_check += character
        string_integer = find_valid_string_digit(string_to_check)
        if string_integer != "":
            integers_in_string += valid_string_digits.get(string_integer)
            string_to_check = reset_string_to_check(string_to_check)
    return integers_in_string


def validate_example():
    """Validate that the processed example input matches the expected output."""
    list_of_decoded_integers = []
    for input_string, expected_integer in zip(example_input, example_output):
        list_of_decoded_integers.append(
            (decode_string(find_all_integers(input_string)))
        )
        assert list_of_decoded_integers[-1] == expected_integer
    assert sum_decoded_integers(list_of_decoded_integers) == sum(example_output)


def solve_puzzle():
    """Solve the puzzle."""
    list_of_decoded_integers = []
    puzzle_input = read_input_file("src/advent_of_code/2023/input/day_01_input.txt")
    for line in puzzle_input:
        list_of_decoded_integers.append((decode_string(find_all_integers(line))))
    return sum_decoded_integers(list_of_decoded_integers)


if __name__ == "__main__":
    validate_example()
    solution = solve_puzzle()
    print(f"The solution to the puzzle is {solution}.")
