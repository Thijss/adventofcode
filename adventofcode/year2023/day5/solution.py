import re
from collections import defaultdict

from adventofcode.lib import load_data

_DATA_INDICES: dict[str, int] = {
    "seed2soil": 1,
    "soil2fert": 2,
    "fert2wat": 3,
    "wat2light": 4,
    "ligth2temp": 5,
    "temp2hum": 6,
    "hum2loc": 7,
}


def part1(file_name: str) -> int:
    data: str = load_data(year=2023, day=5, file_name=file_name)
    data_list: list[str] = data.split("\n\n")

    seeds = list(map(int, re.findall(r"[0-9]+", data_list[0])))

    converters = _get_converters(data_list)
    locations = [_process_value(seed, converters) for seed in seeds]

    return min(locations)


def part2(file_name: str) -> int:
    data: str = load_data(year=2023, day=5, file_name=file_name)
    data_list: list[str] = data.split("\n\n")

    seeds = list(map(int, re.findall(r"[0-9]+", data_list[0])))

    converters = _get_converters(data_list)

    seed_ranges = [range(seeds[idx], seeds[idx] + seeds[idx + 1]) for idx in range(0, len(seeds), 2)]

    # seed_ranges = [seed_ranges[3]]

    for converter in converters.values():
        new_ranges: list[range] = []
        for seed_range in seed_ranges:
            new_ranges += _apply_converters(converter, seed_range)
        seed_ranges = new_ranges

    starts = [seed_range.start for seed_range in seed_ranges]
    return min(starts)


def _get_converters(data_list: list[str]) -> dict[str, list[tuple[range, int]]]:
    converters: dict[str, list[tuple[range, int]]] = defaultdict(list)
    for key, value in _DATA_INDICES.items():
        _, *cdata = data_list[value].split("\n")
        for line in cdata:
            dest, source, length = list(map(int, re.findall(r"[0-9]+", line)))
            mod = dest - source
            converters[key].append((range(source, source + length), mod))
    return converters


def _apply_converters(converter: list[tuple[range, int]], input_range: range) -> list[range]:
    new_ranges: list[range] = []
    modified_ranges: list[range] = []
    for c_range, mod in converter:
        if input_range.stop <= c_range.start:
            continue
        if input_range.start >= c_range.stop:
            continue
        elif input_range.start >= c_range.start and input_range.stop < c_range.stop:
            modified_ranges.append(range(input_range.start, input_range.stop))
            new_ranges.append(range(input_range.start + mod, input_range.stop + mod))
        elif c_range.start <= input_range.start < c_range.stop:
            modified_ranges.append(range(input_range.start, c_range.stop))
            new_ranges.append(range(input_range.start + mod, c_range.stop + mod))
        elif c_range.start <= input_range.stop < c_range.stop:
            modified_ranges.append(range(c_range.start, input_range.stop))
            new_ranges.append(range(c_range.start + mod, input_range.stop + mod))
        elif input_range.start < c_range.start and input_range.stop >= c_range.stop:
            modified_ranges.append(range(c_range.start, c_range.stop))
            new_ranges.append(range(c_range.start + mod, c_range.stop + mod))
        else:
            raise ValueError("This should never happen")

    if not modified_ranges:
        return [input_range]
    if len(input_range) == sum(len(range) for range in modified_ranges):
        return new_ranges

    modified_ranges.sort(key=lambda x: x.start)
    unmodified_ranges: list[range] = []
    for idx in range(len(modified_ranges) - 1):
        if modified_ranges[idx].stop != modified_ranges[idx + 1].start:
            unmodified_ranges.append(range(modified_ranges[idx].stop, modified_ranges[idx + 1].start))

    if input_range.start < (min_modified := min([range.start for range in modified_ranges])):
        unmodified_ranges.append(range(input_range.start, min_modified))
    if input_range.stop > (max_modified := max([range.stop for range in modified_ranges])):
        unmodified_ranges.append(range(max_modified, input_range.stop))
    return unmodified_ranges + new_ranges


def _process_value(value: int, all_ranges: dict[str, list[tuple[range, int]]]) -> int:
    for conversion in _DATA_INDICES.keys():
        for c_range, mod in all_ranges[conversion]:
            if value in c_range:
                value += mod
                break
    return value
