"""Advent of code, 07.12.2023, puzzle 2"""

import re

from day_07_puzzle_1 import (
    example_input,
    generate_df_from_games_dict,
    get_value_of_card,
    get_value_of_hand,
    input_file,
    prepare_input,
)
from input_handling import read_input_file

example_output_total_winnings = 5905


card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
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


def convert_joker_best_possible_card(hand: str) -> str:
    """Convert the joker to the best possible card."""
    number_of_jokers = hand.count("J")
    not_jokers_cards = get_not_jokers_cards(hand)
    if number_of_jokers == 0 or number_of_jokers == 5:  # no jokers or five of a kind
        return hand
    elif number_of_jokers == 4:  # four of a kind
        return hand.replace("J", not_jokers_cards[0])
    else:
        value_of_hand = get_value_of_hand(hand)
        if value_of_hand == 4:  # full house
            return hand.replace("J", not_jokers_cards[0])
        if value_of_hand == 3:  # three of a kind
            if number_of_jokers == 3:
                best_not_joker_card = get_best_not_joker_card(hand)
                return hand.replace("J", best_not_joker_card)
            else:
                most_frequent_card = get_most_frequent_card(hand)
                return hand.replace("J", most_frequent_card)
        else:
            most_frequent_card = get_most_frequent_card(hand)
            return hand.replace("J", most_frequent_card)


def get_not_jokers_cards(hand: str) -> list:
    """Get the cards that are not jokers."""
    return re.findall("[^J]", hand)


def get_best_not_joker_card(hand: str) -> str:
    """Get the best card that is not a joker."""
    not_jokers_cards = get_not_jokers_cards(hand)
    return max(not_jokers_cards, key=lambda x: card_values.get(x))


def get_card_frequency(hand: str) -> dict:
    """Get the most frequent card."""
    hand_dict = {}
    for card in hand:
        hand_dict[card] = hand_dict.get(card, 0) + 1
    return hand_dict


def get_most_frequent_card(hand: str) -> str:
    """Get the most frequent not-joker card. Return the best of those if there are multiple."""
    hand_dict = get_card_frequency(hand.replace("J", ""))
    if max(hand_dict.values()) == 4:
        return [key for (key, value) in hand_dict.items() if value == 4][0]
    elif max(hand_dict.values()) == 3:
        return [key for (key, value) in hand_dict.items() if value == 3][0]
    elif max(hand_dict.values()) == 2:
        cleaned_hand = "".join(
            [key for (key, value) in hand_dict.items() if value == 2]
        )
        return get_best_not_joker_card(cleaned_hand)
    else:
        return get_best_not_joker_card(hand)


def generate_games_dict(raw_input: list) -> dict:
    """Generate a dictionary of games."""
    games_dict = {}
    for i, line in enumerate(raw_input):
        hand, bid = prepare_input(line)
        converted_hand = convert_joker_best_possible_card(hand)
        hand_value = get_value_of_hand(converted_hand)
        games_dict[i] = [hand, bid, hand_value] + [
            get_value_of_card(card, card_values) for card in hand
        ]
    return games_dict


if __name__ == "__main__":
    games_dict = generate_games_dict(example_input)
    games_df = generate_df_from_games_dict(games_dict)
    total_winnings = games_df["winnings"].sum()
    assert total_winnings == example_output_total_winnings
    games_dict = generate_games_dict(read_input_file(input_file))
    games_df = generate_df_from_games_dict(games_dict)
    solution = games_df["winnings"].sum()
    print(f"The solution to the puzzle is {solution}.")
