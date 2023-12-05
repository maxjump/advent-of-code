"""Advent of code, 05.12.2023, puzzle 1"""

import os

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

input_file = os.path.join("2023", "input", "day_05_input.txt")

seed_to_soil_dict = {}
soil_to_fertilizer_dict = {}
fertilizer_to_water_dict = {}
water_to_light_dict = {}
light_to_temperature_dict = {}
temperature_to_humidity_dict = {}
humidity_to_location_dict = {}


def prepare_input(raw_input: list) -> list:
    """Prepare the input string for further processing."""
    list_of_dicts = []
    dict_of_mapping_dicts = {}
    prep_dict = {}
    prep_dict_name = ""
    for line in raw_input:
        if not line:  # line is empty
            continue
        elif ":" in line:
            if "seeds:" in line:  # information for seeds in one single line
                dict_of_mapping_dicts["seeds"] = [
                    int(i) for i in line.split(":")[1].strip().split(" ")
                ]
            elif not prep_dict and not dict_of_mapping_dicts:  # skip line
                continue
            else:
                if prep_dict_name:  # do not add first empty line
                    list_of_dicts.append(prep_dict)
                    dict_of_mapping_dicts[prep_dict_name] = prep_dict
                prep_dict = {}
                prep_dict_name = line.split(":")[0]
        else:
            print(line)
            print(line.split(" "))
            destination_start, source_start, length = line.split(" ")
            min_source, max_source = int(source_start), int(source_start) + int(length)
            min_destination, max_destination = int(destination_start), int(
                destination_start
            ) + int(length)
            prep_dict[(min_source, max_source)] = (min_destination, max_destination)
    list_of_dicts.append(prep_dict)
    # print(list_of_dicts)
    print(dict_of_mapping_dicts)


if __name__ == "__main__":
    prepare_input(example_input)
    prepare_input(read_input_file(input_file))
