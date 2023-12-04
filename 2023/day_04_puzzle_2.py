"""Advent of code, 04.12.2023, puzzle 2"""

from day_04_puzzle_1 import (
    prepare_input,
    check_winning_numbers,
    example_input,
    input_file,
)
from input_handling import read_input_file

example_output = {
    1: 1,
    2: 2,
    3: 4,
    4: 8,
    5: 14,
    6: 1,
}


def generate_scratchcards_dict(number_of_cards: int) -> dict:
    """Generate a dictionary with all scratchcards."""
    scratchcards_dict = {}
    for card_number in range(1, number_of_cards + 1):
        scratchcards_dict[card_number] = 1
    return scratchcards_dict


def update_scratchcards_dict(
    scratchcards_dict: dict, card_number: int, winning_cards: int
) -> dict:
    """Update the scratchcards dictionary."""
    for number in range(card_number + 1, card_number + 1 + winning_cards):
        scratchcards_dict[number] += 1
    return scratchcards_dict


def validate_example() -> None:
    """Validate that the processed example input matches the expected output."""
    scratchcards_dict = generate_scratchcards_dict(len(example_input))
    for input_string in example_input:
        card_number, winning_numbers, elf_numbers = prepare_input(input_string)
        winning_cards = len(check_winning_numbers(elf_numbers, winning_numbers))
        try:
            for number_of_copies in range(1, scratchcards_dict.get(card_number) + 1):
                scratchcards_dict = update_scratchcards_dict(
                    scratchcards_dict, card_number, winning_cards
                )
        except KeyError:  # Scratchcard does not exist
            pass
    assert scratchcards_dict == example_output
    assert sum(scratchcards_dict.values()) == sum(example_output.values())


def solve_puzzle() -> int:
    """Solve the puzzle."""
    puzzle_input = read_input_file(input_file)
    scratchcards_dict = generate_scratchcards_dict(len(puzzle_input))
    for input_string in puzzle_input:
        card_number, winning_numbers, elf_numbers = prepare_input(input_string)
        winning_cards = len(check_winning_numbers(elf_numbers, winning_numbers))
        try:
            for number_of_copies in range(1, scratchcards_dict.get(card_number) + 1):
                scratchcards_dict = update_scratchcards_dict(
                    scratchcards_dict, card_number, winning_cards
                )
        except KeyError:  # Scratchcard does not exist
            pass
    return sum(scratchcards_dict.values())


if __name__ == "__main__":
    validate_example()
    solution = solve_puzzle()
    print(f"The solution to the puzzle is {solution}.")
