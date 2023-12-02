import re

from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2022, day=4, file_name=file_name)
    pairs = data.split("\n")

    overlaps = 0
    for pair in pairs:
        asig1, asig2 = re.findall(r"[0-9]+-[0-9]+", pair)
        rng1 = set(range(int(asig1.split("-")[0]), int(asig1.split("-")[1]) + 1))
        rng2 = set(range(int(asig2.split("-")[0]), int(asig2.split("-")[1]) + 1))
        if rng1.intersection(rng2) in [rng1, rng2]:
            overlaps += 1
    return overlaps


def part2(file_name: str) -> int:
    data = load_data(year=2022, day=4, file_name=file_name)
    pairs = data.split("\n")

    overlaps = 0
    for pair in pairs:
        asig1, asig2 = re.findall(r"[0-9]+-[0-9]+", pair)
        rng1 = set(range(int(asig1.split("-")[0]), int(asig1.split("-")[1]) + 1))
        rng2 = set(range(int(asig2.split("-")[0]), int(asig2.split("-")[1]) + 1))
        if rng1.intersection(rng2):
            overlaps += 1
    return overlaps
