from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2022, day=6, file_name=file_name)
    return _find_marker(data, 4)


def part2(file_name: str) -> int:
    data = load_data(year=2022, day=6, file_name=file_name)
    return _find_marker(data, 14)


def _find_marker(data: str, size: int) -> int:
    marker: list[str] = []
    idx = 0
    for idx, char in enumerate(data):
        if len(marker) < size:
            marker.append(char)
            continue
        if len(set(marker)) == size:
            break
        marker.pop(0)
        marker.append(char)
    return idx
