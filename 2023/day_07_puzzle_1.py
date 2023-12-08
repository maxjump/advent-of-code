"""Advent of code, 07.12.2023, puzzle 1"""

import os

import pandas as pd
from input_handling import read_input_file

example_input = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]
example_output = [1, 4, 3, 2, 5]
example_output_total_winnings = 6440  # 765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5

input_file = os.path.join("2023", "input", "day_07_input.txt")

card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

hand_values = {
    "Five of a kind": 6,
    "Four of a kind": 5,
    "Full house": 4,
    "Three of a kind": 3,
    "Two pair": 2,
    "One pair": 1,
    "High card": 0,
}


def prepare_input(raw_input: str) -> list:
    """Prepare the input string for further processing."""
    split_input = raw_input.split(" ")
    return [split_input[0], int(split_input[1])]


def get_type_of_hand(hand: str) -> str:
    """Get the type of hand."""
    hand_dict = {}
    for card in hand:
        hand_dict[card] = hand_dict.get(card, 0) + 1
    hand_dict = {k: v for k, v in sorted(hand_dict.items(), key=lambda item: item[1])}
    if len(hand_dict) == 1:
        return "Five of a kind"
    elif len(hand_dict) == 2:
        if list(hand_dict.values()) == [1, 4]:
            return "Four of a kind"
        elif list(hand_dict.values()) == [2, 3]:
            return "Full house"
    elif len(hand_dict) == 3:
        if list(hand_dict.values()) == [1, 1, 3]:
            return "Three of a kind"
        elif list(hand_dict.values()) == [1, 2, 2]:
            return "Two pair"
    elif len(hand_dict) == 4:
        return "One pair"
    elif len(hand_dict) == 5:
        return "High card"


def get_value_of_hand(hand: str) -> int:
    """Get the value of a hand."""
    hand_type = get_type_of_hand(hand)
    hand_value = hand_values.get(hand_type)
    return hand_value


def get_value_of_card(card: str, card_values: dict) -> int:
    """Get the value of a card."""
    return card_values.get(card)


def generate_games_dict(raw_input: list) -> dict:
    """Generate a dictionary of games."""
    games_dict = {}
    for i, line in enumerate(raw_input):
        hand, bid = prepare_input(line)
        hand_value = get_value_of_hand(hand)
        games_dict[i] = [hand, bid, hand_value] + [
            get_value_of_card(card, card_values) for card in hand
        ]
    return games_dict


def generate_df_from_games_dict(games_dict: dict) -> pd.DataFrame:
    """Generate a dataframe from a dictionary of games."""
    games_df = pd.DataFrame.from_dict(games_dict).T
    games_df.columns = [
        "hand",
        "bid",
        "hand_value",
        "card_value_1",
        "card_value_2",
        "card_value_3",
        "card_value_4",
        "card_value_5",
    ]
    games_df.sort_values(
        by=[
            "hand_value",
            "card_value_1",
            "card_value_2",
            "card_value_3",
            "card_value_4",
            "card_value_5",
        ],
        ascending=True,
        inplace=True,
    )
    games_df.reset_index(drop=True, inplace=True)
    games_df.index += 1
    games_df["winnings"] = games_df["bid"] * games_df.index
    return games_df


if __name__ == "__main__":
    games_dict = generate_games_dict(example_input)
    games_df = generate_df_from_games_dict(games_dict)
    total_winnings = games_df["winnings"].sum()
    assert total_winnings == example_output_total_winnings
    games_dict = generate_games_dict(read_input_file(input_file))
    games_df = generate_df_from_games_dict(games_dict)
    solution = games_df["winnings"].sum()
    print(f"The solution to the puzzle is {solution}.")
