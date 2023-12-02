"""Advent of code, 02.12.2023, puzzle 1"""

import os

from input_handling import read_input_file

example_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
example_output = [True, True, False, False, True]
example_sum = 8

input_file = os.path.join("2023", "input", "day_02_input.txt")

cubes_in_game = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def handle_raw_input(raw_input: str) -> list[int, str]:
    """Split the raw input string to obtain the game number and rounds."""
    first_split = raw_input.split(":")
    game_number = int(first_split[0].split(" ")[1])
    rounds = first_split[1].split(";")
    return [game_number, rounds]


def transform_round_information(raw_round: str) -> dict[str:int]:
    """Transform the raw information of a round into a dictionary."""
    cubes_dict = {}
    raw_cubes = (single_round.strip() for single_round in raw_round.split(","))
    for raw_cube in raw_cubes:
        for color in cubes_in_game.keys():
            if color in raw_cube:
                cubes_dict[color] = int(raw_cube.split(" ")[0])
    return cubes_dict


def check_game_possible(raw_game: str) -> bool:
    """Check whether a game with the given number of cubes is possible."""
    for raw_round in raw_game:
        cubes_dict = transform_round_information(raw_round)
        for color in cubes_in_game.keys():
            if cubes_dict.get(color, 0) > cubes_in_game.get(color):
                return False
    return True


def validate_example() -> None:
    """Validate that the processed example input matches the expected output."""
    game_possible_list = []
    possible_game_numbers = []
    for example in example_input:
        game_number, game_input = handle_raw_input(example)
        game_possible = check_game_possible(game_input)
        game_possible_list.append(game_possible)
        if game_possible:
            possible_game_numbers.append(game_number)
    assert game_possible_list == example_output
    assert sum(possible_game_numbers) == example_sum


def solve_puzzle() -> int:
    """Solve the puzzle."""
    possible_game_numbers = []
    puzzle_input = read_input_file(input_file)
    for example in puzzle_input:
        game_number, game_input = handle_raw_input(example)
        if check_game_possible(game_input):
            possible_game_numbers.append(game_number)
    return sum(possible_game_numbers)


if __name__ == "__main__":
    validate_example()
    solution = solve_puzzle()
    print(f"The solution to the puzzle is {solution}.")
