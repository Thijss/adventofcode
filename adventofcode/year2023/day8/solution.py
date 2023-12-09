import re

from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=8, file_name=file_name)

    instructions, reference_str = data.split("\n\n")
    references: dict[str, tuple[str, str]] = _parse_references(reference_str)

    key: str = "AAA"
    step_count = 0
    while key != "ZZZ":
        for inst in instructions:
            lvalue, rvalue = references[key]
            key = lvalue if inst == "L" else rvalue
            step_count += 1
    return step_count


def part2(file_name: str) -> int:
    return 1


def _parse_references(reference_str: str) -> dict[str, tuple[str, str]]:
    references: dict[str, tuple[str, str]] = {}
    for line in reference_str.splitlines():
        key, lvalue, rvalue = re.findall(r"[A-Z]+", line)
        references[key] = (lvalue, rvalue)
    return references
