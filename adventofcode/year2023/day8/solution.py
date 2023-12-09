import re
from math import lcm

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
    data = load_data(year=2023, day=8, file_name=file_name)

    instruction_str, reference_str = data.split("\n\n")
    instruction_str = instruction_str.replace("L", "0").replace("R", "1")
    instructions: list[int] = [int(inst) for inst in instruction_str]
    references: dict[str, tuple[str, str]] = _parse_references(reference_str)

    a_keys = [key for key in references.keys() if key.endswith("A")]

    steps = [_count_steps(instructions, references, key) for key in a_keys]
    return lcm(*steps)


def _count_steps(instructions: list[int], references: dict[str, tuple[str, str]], key: str) -> int:
    step_count = 0
    while not key.endswith("Z"):
        for inst in instructions:
            step_count += 1
            key = references[key][inst]
    return step_count


def _parse_references(reference_str: str) -> dict[str, tuple[str, str]]:
    references: dict[str, tuple[str, str]] = {}
    for line in reference_str.splitlines():
        key, lvalue, rvalue = re.findall(r"[0-9A-Z]+", line)
        references[key] = (lvalue, rvalue)
    return references
