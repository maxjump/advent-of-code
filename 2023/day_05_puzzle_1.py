"""Advent of code, 05.12.2023, puzzle 1"""

import os
from typing import Callable
from input_handling import read_input_file

example_input = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]

example_output = [
    [79, 81, 81, 81, 74, 78, 78, 82],
    [14, 14, 53, 49, 42, 42, 43, 43],
    [55, 57, 57, 53, 46, 82, 82, 86],
    [13, 13, 52, 41, 34, 34, 35, 35],
]
example_min_location = 35
input_file = os.path.join("2023", "input", "day_05_input.txt")

mapping_order = [
    "seed-to-soil map",
    "soil-to-fertilizer map",
    "fertilizer-to-water map",
    "water-to-light map",
    "light-to-temperature map",
    "temperature-to-humidity map",
    "humidity-to-location map",
]


def prepare_seed_line(seed_line: str) -> list:
    """Prepare the seed line for further processing."""
    return [int(i) for i in seed_line.split(":")[1].strip().split(" ")]


def prepare_input(raw_input: list, seed_preparation: Callable) -> dict:
    """Prepare the input string for further processing."""
    dict_of_mapping_dicts = {}
    prep_dict = {}
    prep_dict_name = ""
    for line in raw_input:
        if not line:  # line is empty
            continue
        elif ":" in line:
            if "seeds:" in line:  # information for seeds in one single line
                dict_of_mapping_dicts["seeds"] = seed_preparation(line)
            elif not prep_dict and not dict_of_mapping_dicts:  # skip line
                continue
            else:
                if prep_dict_name:  # do not add first empty line
                    dict_of_mapping_dicts[prep_dict_name] = prep_dict
                prep_dict = {}
                prep_dict_name = line.split(":")[0]
        else:
            destination_start, source_start, length = line.split(" ")
            min_source, max_source = int(source_start), int(source_start) + int(length)
            min_destination, max_destination = int(destination_start), int(
                destination_start
            ) + int(length)
            prep_dict[(min_source, max_source)] = (min_destination, max_destination)
    dict_of_mapping_dicts[prep_dict_name] = prep_dict
    return dict_of_mapping_dicts


def get_destination_for_source(source: int, mapping: dict) -> int:
    """Get the destination for a given source."""
    for source_range, destination_range in mapping.items():
        if source in range(source_range[0], source_range[1]):
            return destination_range[0] + (source - source_range[0])
    return source


def get_mapping_for_seed(seed: int, mapping: dict):
    """Get the location for a given seed."""
    mapping_list = [seed]
    for map_order in mapping_order:
        mapping_list.append(
            get_destination_for_source(mapping_list[-1], mapping.get(map_order))
        )
    return mapping_list


def get_mapping_for_all_seeds(seeds: list, mapping: dict):
    """Get the location for all given seeds."""
    mapping_list = []
    for seed in seeds:
        mapping_list.append(get_mapping_for_seed(seed, mapping))
    return mapping_list


def get_minimum_location(mapping_list: list) -> int:
    """Get the minimum location for a given mapping list."""
    return min([i[-1] for i in mapping_list])


if __name__ == "__main__":
    mapping_dict = prepare_input(example_input, prepare_seed_line)
    mapping_list = get_mapping_for_all_seeds(mapping_dict.get("seeds"), mapping_dict)
    assert mapping_list == example_output
    assert get_minimum_location(mapping_list) == example_min_location
    mapping_dict = prepare_input(read_input_file(input_file), prepare_seed_line)
    mapping_list = get_mapping_for_all_seeds(mapping_dict.get("seeds"), mapping_dict)
    solution = get_minimum_location(mapping_list)
    print(f"The solution to the puzzle is {solution}.")
