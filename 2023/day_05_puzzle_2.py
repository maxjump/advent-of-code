"""Advent of code, 05.12.2023, puzzle 2"""

from day_05_puzzle_1 import example_input, input_file, prepare_input, mapping_order, get_destination_for_source
from input_handling import read_input_file

example_output = 46


def prepare_seed_line(seed_line: str) -> list:
    """Prepare the seed line for further processing."""
    integers = [int(i) for i in seed_line.split(":")[1].strip().split(" ")]
    tuples_list = [range(integers[i], integers[i] + integers[i + 1]) for i in range(0, len(integers), 2) if i + 1 < len(integers)]
    return tuples_list


def get_location_for_seed(seed: int, mapping: dict):
    """Get the location for a given seed."""
    mapping_list = [seed]
    for map_order in mapping_order:
        mapping_list.append(
            get_destination_for_source(mapping_list[-1], mapping.get(map_order))
        )
    return mapping_list[-1]


def get_minimum_location(seed_ranges: list, mapping: dict) -> int:
    """Get the minimum location for all seeds."""
    min_location = None
    for seed_range in seed_ranges:
        print(seed_range)
        for seed in seed_range:
            location = get_location_for_seed(seed, mapping)
            if not min_location:
                min_location = location
            elif location < min_location:
                min_location = location
    return min_location


# TODO: change dictionaries to contain only one range, if possible
# alternatively, sort the ranges to allow for easier checks


if __name__ == "__main__":
    mapping_dict = prepare_input(example_input, prepare_seed_line)
    minimum_location = get_minimum_location(mapping_dict.get("seeds"), mapping_dict)
    assert minimum_location == example_output
    mapping_dict = prepare_input(read_input_file(input_file), prepare_seed_line)
    solution = get_minimum_location(mapping_dict.get("seeds"), mapping_dict)
    print(f"The solution to the puzzle is {solution}.")
