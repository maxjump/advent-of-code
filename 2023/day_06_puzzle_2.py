"""Advent of code, 06.12.2023, puzzle 2"""

from day_06_puzzle_1 import calculate_ways_to_win_race, example_input, input_file
from input_handling import read_input_file

example_output = 71503


def prepare_input(raw_input: list) -> (int, int):
    """Prepare the input string for further processing."""
    race_time = "".join([i for i in raw_input[0].split(":")[1].strip().split()])
    race_distance = "".join([i for i in raw_input[1].split(":")[1].strip().split()])
    return int(race_time), int(race_distance)


if __name__ == "__main__":
    time, distance = prepare_input(example_input)
    ways_to_win = calculate_ways_to_win_race(time, distance)
    assert ways_to_win == example_output
    time, distance = prepare_input(read_input_file(input_file))
    solution = calculate_ways_to_win_race(time, distance)
    print(f"The solution to the puzzle is {solution}.")
