import math
import re

from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data: str = load_data(year=2023, day=6, file_name=file_name)
    time_str, distance_str = data.split("\n")
    times: list[int] = list(map(int, re.findall(r"[0-9]+", time_str)))
    distances: list[int] = list(map(int, re.findall(r"[0-9]+", distance_str)))

    n_wins: list[int] = []
    for time, distance in zip(times, distances):
        n_wins.append(_find_optimum_with_skip(time, distance))

    return math.prod(n_wins)


def part2(file_name: str) -> int:
    data: str = load_data(year=2023, day=6, file_name=file_name)
    time_str, distance_str = data.split("\n")
    time = int(time_str.split(":")[1].replace(" ", ""))
    distance = int(distance_str.split(":")[1].replace(" ", ""))

    return _find_optimum_with_skip(time, distance)


def _find_optimum_with_skip(time: int, distance: int) -> int:
    start = -1
    for hold in range(time):
        speed = hold
        new_distance = speed * (time - hold)
        if new_distance > distance:
            start = hold
            break

    end = -1
    for hold in range(time - 1, start, -1):
        speed = hold
        new_distance = speed * (time - hold)
        if new_distance > distance:
            end = hold
            break

    return len(range(start, end + 1))
