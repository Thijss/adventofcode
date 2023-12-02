import re

from adventofcode.lib import load_data


def part1(file_name: str) -> str:
    data = load_data(year=2022, day=5, file_name=file_name)
    crates, moves = data.split("\n\n")
    *crates, _ = crates.split("\n")
    stacks = _build_stacks(crates)

    instructions = _parse_moves(moves)

    _apply_instructions(stacks, instructions, reverse=True)
    message = "".join([stack.pop() for stack in stacks.values() if stack])
    return message


def part2(file_name: str) -> str:
    data = load_data(year=2022, day=5, file_name=file_name)
    crates, moves = data.split("\n\n")
    *crates, _ = crates.split("\n")
    stacks = _build_stacks(crates)

    instructions = _parse_moves(moves)

    _apply_instructions(stacks, instructions, reverse=False)
    message = "".join([stack.pop() for stack in stacks.values() if stack])
    return message


def _build_stacks(crates: list[str]) -> dict[int, list[str]]:
    start_indices = range(0, len(crates[0]), 4)

    stacks: dict[int, list[str]] = {i: [] for i in range(1, len(start_indices) + 1)}

    for row in crates[::-1]:
        row_crates = [row[i : i + 3] for i in start_indices]
        for idx, crate in enumerate(row_crates):
            if re.match(r"\[[A-Z]\]", crate):
                stacks[idx + 1].append(crate.replace("]", "").replace("[", ""))
    return stacks


def _parse_moves(moves: str) -> list[tuple[int, ...]]:
    return [tuple(map(int, re.findall(r"[0-9]+", move))) for move in moves.split("\n")]


def _apply_instructions(stacks: dict[int, list[str]], instructions: list[tuple[int, ...]], reverse: bool) -> None:
    for amount, from_stack, to_stack in instructions:
        crates = stacks[from_stack][-amount:]
        if reverse:
            crates.reverse()
        stacks[to_stack].extend(crates)
        stacks[from_stack] = stacks[from_stack][:-amount]
