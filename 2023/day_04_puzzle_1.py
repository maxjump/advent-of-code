"""Advent of code, 04.12.2023, puzzle 1"""

import os

from input_handling import read_input_file

example_input = [
    "Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

example_output = [
    [17, 48, 83, 86],
    [32, 61],
    [1, 21],
    [84],
    [],
    [],
]

example_output_points = [8, 2, 2, 1, 0, 0]

input_file = os.path.join("2023", "input", "day_04_input.txt")


def prepare_input(input_string: str) -> list:
    """Prepare the input string for further processing."""
    first_split = input_string.split(":")
    card_number = int(first_split[0].split(" ")[-1])
    second_split = first_split[1].split("|")
    winning_numbers = [i for i in second_split[0].strip().split(" ") if i]
    winning_numbers = [int(i) for i in winning_numbers]
    elf_numbers = [i for i in second_split[1].strip().split(" ") if i]
    elf_numbers = [int(i) for i in elf_numbers]
    return [card_number, winning_numbers, elf_numbers]


def check_winning_numbers(elf_numbers: list, winning_numbers: list) -> list:
    """Check if the elf's numbers are winning numbers."""
    elf_winning_numbers = []
    for number in elf_numbers:
        if number in winning_numbers:
            elf_winning_numbers.append(number)
    return sorted(elf_winning_numbers)


def calculate_points(elf_winning_numbers: list) -> int:
    """Calculate the points for a card."""
    power = len(elf_winning_numbers) - 1
    return 2**power if power >= 0 else 0


def validate_example() -> None:
    """Validate that the processed example input matches the expected output."""
    points = 0
    for input_string, expected_output in zip(example_input, example_output):
        card_number, winning_numbers, elf_numbers = prepare_input(input_string)
        elf_winning_numbers = check_winning_numbers(elf_numbers, winning_numbers)
        assert elf_winning_numbers == expected_output
        elf_points = calculate_points(elf_winning_numbers)
        assert elf_points == example_output_points[card_number - 1]
        points += elf_points
    assert points == sum(example_output_points)


def solve_puzzle() -> int:
    """Solve the puzzle."""
    points = 0
    puzzle_input = read_input_file(input_file)
    for input_string in puzzle_input:
        card_number, winning_numbers, elf_numbers = prepare_input(input_string)
        elf_winning_numbers = check_winning_numbers(elf_numbers, winning_numbers)
        elf_points = calculate_points(elf_winning_numbers)
        points += elf_points
    return points


if __name__ == "__main__":
    validate_example()
    solution = solve_puzzle()
    print(f"The solution to the puzzle is {solution}.")
