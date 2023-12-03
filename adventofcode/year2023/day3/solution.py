import re

from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=3, file_name=file_name)

    data_dict: dict[int, str] = {idx: line for idx, line in enumerate(data.split("\n"))}

    start_dict: dict[int, list[tuple[int, int]]] = {}
    for idx, line in data_dict.items():
        start_dict[idx] = [(m.start(), m.end()) for m in re.finditer(r"[0-9]+", line)]

    total = 0
    for line, numbers in start_dict.items():
        for start, end in numbers:
            number = int(data_dict[line][start:end])
            start_idx = max(0, start - 1)
            end_idx = min(len(data_dict[line]) - 1, end + 1)

            if _adjacent_symbol(data_dict, line, start_idx, end_idx):
                print(number)
                total += number
    return total


def part2(file_name: str) -> int:
    data = load_data(year=2023, day=3, file_name=file_name)
    return len(data)


def _adjacent_symbol(data_dict: dict[int, str], line: int, start: int, end: int) -> bool:
    symbol_above = _symbol_above(data_dict, line, start, end)
    symbol_below = _symbol_below(data_dict, line, start, end)
    symbol_left_or_right = _symbol_left_or_right(data_dict, line, start, end)
    return symbol_above or symbol_below or symbol_left_or_right


def _symbol_above(data_dict: dict[int, str], line: int, start: int, end: int) -> bool:
    return bool(line > 0 and re.findall(r"[^.]", data_dict[line - 1][start:end]))


def _symbol_below(data_dict: dict[int, str], line: int, start: int, end: int) -> bool:
    return bool(line < len(data_dict) - 1 and re.findall(r"[^.]", data_dict[line + 1][start:end]))


def _symbol_left_or_right(data_dict: dict[int, str], line: int, start: int, end: int) -> bool:
    left = data_dict[line][start] != "." if start > 0 else False
    right = data_dict[line][end - 1] != "." if end < len(data_dict[line]) - 1 else False
    return left or right
