"""Advent of code, 06.12.2023, puzzle 1"""

import math
import os

from input_handling import read_input_file

example_input = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]
example_output = [4, 8, 9]
example_output_ways_to_win = 288  # 4 * 8 * 9


input_file = os.path.join("2023", "input", "day_06_input.txt")


def prepare_input(raw_input: list) -> dict:
    """Prepare the input string for further processing."""
    times = [int(i) for i in raw_input[0].split(":")[1].strip().split()]
    distances = [int(i) for i in raw_input[1].split(":")[1].strip().split()]
    race_dict = dict(zip(times, distances))
    return race_dict


def calculate_ways_to_win_race(race_time: int, race_distance: int) -> int:
    """Calculate the number of ways to win one race."""
    ways_to_win = 0
    for i in range(0, race_time + 1):
        speed = i
        distance_travelled = speed * (race_time - i)
        if distance_travelled > race_distance:
            ways_to_win += 1
    return ways_to_win


def calculate_ways_to_win_all_races(race_dict: dict) -> (int, list):
    """Calculate the number of ways to win all races."""
    ways_to_win_list = []
    for race_time, race_distance in race_dict.items():
        ways_to_win_list.append(calculate_ways_to_win_race(race_time, race_distance))
    return math.prod(ways_to_win_list), ways_to_win_list


if __name__ == "__main__":
    race_dict = prepare_input(example_input)
    example_ways_to_win, example_ways_to_win_list = calculate_ways_to_win_all_races(
        race_dict
    )
    assert example_ways_to_win == example_output_ways_to_win
    assert example_ways_to_win_list == example_output
    race_dict = prepare_input(read_input_file(input_file))
    solution, _ = calculate_ways_to_win_all_races(race_dict)
    print(f"The solution to the puzzle is {solution}.")
