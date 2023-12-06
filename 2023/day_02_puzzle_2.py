"""Advent of code, 02.12.2023, puzzle 2"""

import math

from day_02_puzzle_1 import (example_input, handle_raw_input, input_file,
                             transform_round_information)
from input_handling import read_input_file

example_output = [48, 12, 1560, 630, 36]


def get_maximum_number_of_cubes_in_game(raw_game: str) -> dict[str:int]:
    """Return the maximum number of cubes from a game."""
    cubes_power_dict = {"red": 0, "green": 0, "blue": 0}
    for raw_round in raw_game:
        cubes_dict = transform_round_information(raw_round)
        for color in cubes_power_dict.keys():
            if cubes_dict.get(color, 0) > cubes_power_dict.get(color):
                cubes_power_dict[color] = cubes_dict.get(color)
    return cubes_power_dict


def calculate_power_of_set(cubes_power_dict: dict[str:int]) -> int:
    """Calculate the power of a set of cubes."""
    return math.prod(cubes_power_dict.values())


def validate_example() -> None:
    """Validate that the processed example input matches the expected output."""
    game_powers = []
    for example in example_input:
        game_number, game_input = handle_raw_input(example)
        game_powers.append(
            calculate_power_of_set(get_maximum_number_of_cubes_in_game(game_input))
        )
    assert sum(game_powers) == sum(example_output)


def solve_puzzle() -> int:
    """Solve the puzzle."""
    game_powers = []
    puzzle_input = read_input_file(input_file)
    for example in puzzle_input:
        game_number, game_input = handle_raw_input(example)
        game_powers.append(
            calculate_power_of_set(get_maximum_number_of_cubes_in_game(game_input))
        )
    return sum(game_powers)


if __name__ == "__main__":
    validate_example()
    solution = solve_puzzle()
    print(f"The solution to the puzzle is {solution}.")
