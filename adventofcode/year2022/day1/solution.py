from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2022, day=1, file_name=file_name)
    
    return count_calories(data)[0]


def part2(file_name: str) -> int:
    data = load_data(year=2022, day=1, file_name=file_name)
    return sum(count_calories(data)[:3])


def count_calories(data: str) -> list[int]:
    data = data.replace("\n\n", "🎅")

    all_calories: list[int] = []
    for elf in data.split("🎅"):
        elf_calories = sum([int(x) for x in elf.split("\n")])
        all_calories.append(elf_calories)
    all_calories.sort()
    all_calories.reverse()
    return all_calories
