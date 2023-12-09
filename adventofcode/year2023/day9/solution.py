from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=9, file_name=file_name)
    histories = [list(map(int, line.split(" "))) for line in data.splitlines()]

    total = 0
    for history in histories:
        total += _find_next_value(history)
    return total


def part2(file_name: str) -> int:
    data = load_data(year=2023, day=9, file_name=file_name)
    return 0


def _find_next_value(history: list[int]) -> int:
    diff_dict: dict[int, list[int]] = {0: history}
    index = 1
    while True:
        diff = _find_diffs(history)
        diff_dict[index] = diff
        index += 1
        history = diff
        if set(diff) == {0}:
            break

    for idx in range(len(diff_dict) - 2, -1, -1):
        last_value = diff_dict[idx][-1]
        print(idx)
        diff_value = diff_dict[idx + 1][-1]
        diff_dict[idx].append(last_value + diff_value)
    return diff_dict[0][-1]


def _find_diffs(numbers: list[int]):
    return [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
