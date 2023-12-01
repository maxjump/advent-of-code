"""Advent of code, 01.12.2023, puzzle 1"""

from input_handling import read_input_file


example_input = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

example_output = [12, 38, 15, 77]


def check_integer_in_string(part_of_string: str) -> str:
    """Convert a string to an integer."""
    try:
        _ = int(part_of_string)
        return part_of_string
    except ValueError:
        return ""


def find_integers_in_string(input_string: str) -> str:
    """Find all integers in a string."""
    integers_in_string = ""
    for character in input_string:
        integers_in_string += check_integer_in_string(character)
    return integers_in_string


def decode_string(integer_string: str) -> int:
    """Decode a string to return the first and last number contained as one integer."""
    return int(integer_string[0] + integer_string[-1])


def sum_decoded_integers(list_of_decoded_integers: list) -> int:
    """Sum all integers in a list."""
    return sum(list_of_decoded_integers)


def validate_example():
    """Validate that the processed example input matches the expected output."""
    list_of_decoded_integers = []
    for input_string, expected_integer in zip(example_input, example_output):
        list_of_decoded_integers.append(
            (decode_string(find_integers_in_string(input_string)))
        )
        assert list_of_decoded_integers[-1] == expected_integer
    assert sum_decoded_integers(list_of_decoded_integers) == sum(example_output)


def solve_puzzle():
    """Solve the puzzle."""
    list_of_decoded_integers = []
    puzzle_input = read_input_file("src/advent_of_code/2023/input/day_01_input.txt")
    for line in puzzle_input:
        list_of_decoded_integers.append((decode_string(find_integers_in_string(line))))
    return sum_decoded_integers(list_of_decoded_integers)


if __name__ == "__main__":
    validate_example()
    solution = solve_puzzle()
    print(f"The solution to the puzzle is {solution}.")
