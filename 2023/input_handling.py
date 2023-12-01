"""Handle input files."""


def read_input_file(input_file_path: str) -> list:
    """Read an input file and return a list of strings."""
    with open(input_file_path, "r") as input_file:
        input_list = input_file.read().splitlines()
    return input_list
