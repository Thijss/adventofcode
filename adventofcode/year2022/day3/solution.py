import re
from string import ascii_lowercase as alphabet

from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2022, day=3, file_name=file_name)

    sum = 0
    for bag in data.split("\n"):
        container1, container2 = bag[: len(bag) // 2], bag[len(bag) // 2 :]
        item = (set(container1) & set(container2)).pop()
        prio = _calculate_prio(item)
        sum += prio
    return sum


def part2(file_name: str) -> int:
    data = load_data(year=2022, day=3, file_name=file_name)
    data = data.replace("\n", "🎅")
    groups = re.findall(r"(\w+)🎅(\w+)🎅(\w+)", data)
    sum = 0
    for group in groups:
        badge = (set(group[0]) & set(group[1]) & set(group[2])).pop()
        prio = _calculate_prio(badge)
        sum += prio
    return sum


def _calculate_prio(letter: str) -> int:
    if letter.isupper():
        return (alphabet.index(letter.lower()) + 1) + 26
    return alphabet.index(letter) + 1
