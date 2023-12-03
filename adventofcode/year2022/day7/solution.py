from collections import Counter
from pathlib import Path, PosixPath

from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2022, day=7, file_name=file_name)
    dir_counter = _build_dir_counter(data)
    return sum([size for size in dir_counter.values() if size <= 100000])


def part2(file_name: str) -> int:
    data = load_data(year=2022, day=7, file_name=file_name)
    dir_counter = _build_dir_counter(data)
    unused_space = 70000000 - dir_counter["/"]
    required_space = 30000000 - unused_space

    smallest = 30000000
    for size in dir_counter.values():
        if size > required_space and size < smallest:
            smallest = size
    return smallest


def _build_dir_counter(data: str) -> Counter[str]:
    dir_counter: Counter[str] = Counter()
    cwd: Path = PosixPath("/")
    counted: set[str] = set()
    for line in data.split("\n"):
        line = line.replace("\n", "")
        if line.startswith("dir") or line == "$ ls":
            continue
        elif line == "$ cd /":
            cwd = Path("/")
        elif line == "$ cd ..":
            cwd = cwd.parent
        elif line.startswith("$ cd "):
            cwd = cwd / line.replace("$ cd ", "")
        elif line[0].isdigit():
            size, name = line.split(" ")
            if str(cwd / name) in counted:
                continue
            _count_file(dir_counter, cwd, int(size))
            counted.add(str(cwd / name))
        else:
            raise ValueError(f"Unknown line: {line}")
    return dir_counter


def _count_file(dir_counter: Counter[str], path: Path, size: int) -> None:
    while str(path) != "/":
        dir_counter[str(path)] += size
        path = path.parent

    dir_counter["/"] += size
