"""Advent of code, 08.12.2023, puzzle 1"""

import os

from input_handling import read_input_file

example_input = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]
example_output = 6

input_file = os.path.join("2023", "input", "day_08_input.txt")


def prepare_input(raw_input: str) -> str | dict:
    """Prepare the input string for further processing."""
    if "=" in raw_input:
        split_input = raw_input.split(" = ")
        start = split_input[0]
        end = split_input[1].strip("()").split(", ")
        return {start: end}


def generate_network_dict(raw_input: list[str]) -> dict:
    """Generate a dictionary representing the network."""
    network_dict = {}
    for line in raw_input:
        if line:
            network_dict.update(prepare_input(line))
    return network_dict


def find_next_node(current_node: str, direction: str) -> int:
    """Find the next node."""
    if direction == "L":
        next_node = network_dict[current_node][0]
    elif direction == "R":
        next_node = network_dict[current_node][1]
    return next_node


def find_path(directions: str) -> list:
    """Find the path."""
    path = []
    current_node = "AAA"
    while current_node != "ZZZ":
        for direction in directions:
            next_node = find_next_node(current_node, direction)
            path.append(next_node)
            current_node = next_node
            if current_node == "ZZZ":
                break
    return path


def get_length_of_path(path: list) -> int:
    """Get the length of the path."""
    return len(path)


if __name__ == "__main__":
    directions = example_input[0]
    network_dict = generate_network_dict(example_input[2:])
    path = find_path(directions)
    length_of_path = get_length_of_path(path)
    assert length_of_path == example_output
    puzzle_input = read_input_file(input_file)
    directions = puzzle_input[0]
    network_dict = generate_network_dict(puzzle_input[2:])
    path = find_path(directions)
    solution = get_length_of_path(path)
    print(f"The solution to the puzzle is {solution}.")
