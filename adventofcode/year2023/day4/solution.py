import re

from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=4, file_name=file_name)
    score = 0
    for line in data.split("\n"):
        _, line = line.split(":")
        wins, card = line.split("|")
        wins = set(map(int, re.findall(r"\d+", wins)))
        card = set(map(int, re.findall(r"\d+", card)))
        result = wins.intersection(card)
        score += 2 ** (len(result) - 1) if result else 0
    return score


def part2(file_name: str) -> int:
    data = load_data(year=2023, day=4, file_name=file_name)
    return 0
