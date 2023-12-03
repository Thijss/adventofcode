import re
from math import prod

from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=3, file_name=file_name)

    data_dict: dict[int, str] = {idx: line for idx, line in enumerate(data.split("\n"))}

    number_dict: dict[int, list[tuple[int, int]]] = {}
    for idx, line in data_dict.items():
        number_dict[idx] = [(m.start(), m.end()) for m in re.finditer(r"[0-9]+", line)]

    total = 0
    for line, numbers in number_dict.items():
        for start, end in numbers:
            number = int(data_dict[line][start:end])
            start_idx = max(0, start - 1)
            end_idx = min(len(data_dict[line]) - 1, end)

            for line_mod in [-1, 0, 1]:
                if _find_symbol(data_dict, line + line_mod, start_idx, end_idx):
                    total += number
                    break

    return total


def part2(file_name: str) -> int:
    data = load_data(year=2023, day=3, file_name=file_name)
    data_dict: dict[int, str] = {idx: line for idx, line in enumerate(data.split("\n"))}

    gear_dict: dict[int, list[int]] = {}
    for idx, line in data_dict.items():
        gear_dict[idx] = [m.start() for m in re.finditer(r"\*", line)]

    number_dict: dict[int, list[tuple[int, int]]] = {}
    for idx, line in data_dict.items():
        number_dict[idx] = [(m.start(), m.end()) for m in re.finditer(r"[0-9]+", line)]

    total = 0
    for line, gears in gear_dict.items():
        for gear_idx in gears:
            start_idx = max(0, gear_idx - 1)
            end_idx = min(len(data_dict[line]) - 1, gear_idx + 1)
            search_range = set(range(start_idx, end_idx + 1))

            numbers_above = _find_numbers(data_dict, number_dict, line - 1, search_range)
            numbers_below = _find_numbers(data_dict, number_dict, line + 1, search_range)
            numbers_same_line = _find_numbers(data_dict, number_dict, line, search_range)
            linked_numbers = numbers_above + numbers_below + numbers_same_line
            if len(linked_numbers) == 2:
                total += prod(linked_numbers)
    return total


def _find_symbol(data_dict: dict[int, str], line: int, start: int, end: int) -> bool:
    if line in [-1, len(data_dict)]:
        return False
    return bool(re.findall(r"[^.0-9]", data_dict[line][start : end + 1]))


def _find_numbers(
    data_dict: dict[int, str], number_dict: dict[int, list[tuple[int, int]]], line: int, search_range: set[int]
) -> list[int]:
    if line in [-1, len(data_dict)]:
        return []
    numbers = number_dict[line]
    matching_numbers = [number for number in numbers if set(range(*number)).intersection(search_range)]

    if len(matching_numbers) == 0:
        return []
    return [int(data_dict[line][start:end]) for start, end in matching_numbers]
