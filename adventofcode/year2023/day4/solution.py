import re
from collections import Counter

from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=4, file_name=file_name)
    score = 0

    card_dict = _build_card_dict(data)

    for numbers, wins in card_dict.values():
        result = wins.intersection(numbers)
        score += 2 ** (len(result) - 1) if result else 0
    return score


def part2(file_name: str) -> int:
    data = load_data(year=2023, day=4, file_name=file_name)
    card_dict = _build_card_dict(data)
    copies: Counter[int] = Counter()

    for card_nr, (wins, numbers) in card_dict.items():
        result = len(wins.intersection(numbers))
        if result:
            n_copies = copies.get(card_nr, 0) + 1

            for card_nr_win in range(card_nr + 1, card_nr + result + 1):
                copies[card_nr_win] += n_copies
    return sum(copies.values()) + len(card_dict)


def _build_card_dict(data: str) -> dict[int, tuple[set[int], set[int]]]:
    card_dict: dict[int, tuple[set[int], set[int]]] = {}
    for line in data.split("\n"):
        card, line = line.split(":")
        card_nr = int(re.findall(r"\d+", card).pop())
        wins, numbers = line.split("|")
        wins = set(map(int, re.findall(r"\d+", wins)))
        numbers = set(map(int, re.findall(r"\d+", numbers)))
        card_dict[card_nr] = (wins, numbers)
    return card_dict
