from adventofcode.lib import load_data


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=1, file_name=file_name)
    data = "".join([x for x in data if x in "1234567890\n"])
    data = data.split("\n")
    return sum([int(x[0] + x[-1]) for x in data])


_STRING2INT = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

_INT2STRING = {v: k for k, v in _STRING2INT.items()}


def part2(file_name: str) -> int:
    data = load_data(year=2023, day=1, file_name=file_name)

    for digit, string in _INT2STRING.items():
        data = data.replace(str(digit), string)

    data = data.split("\n")
    total_sum = 0
    for line in data:
        first_digit = _find_first_digit(line)
        last_digit = _find_last_digit(line)
        total_sum += int(str(first_digit) + str(last_digit))
    return total_sum


def _find_first_digit(line: str) -> int:
    first_digit = -1
    lowest_index = len(line)

    for word in _STRING2INT.keys():
        index = line.find(word)
        if index != -1 and index < lowest_index:
            lowest_index = index
            first_digit = _STRING2INT[word]

    if first_digit == -1:
        raise ValueError(f"Could not find first digit in line: {line}")
    return first_digit


def _find_last_digit(line: str) -> int:
    last_digit = -1
    lowest_index = len(line)

    for word in _STRING2INT.keys():
        index = line[::-1].find(word[::-1])
        if index != -1 and index < lowest_index:
            lowest_index = index
            last_digit = _STRING2INT[word]

    if last_digit == -1:
        raise ValueError(f"Could not find last digit in line: {line}")
    return last_digit
