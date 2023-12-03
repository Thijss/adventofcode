from adventofcode.year2023.day3.solution import part1, part2


def test_day1_part1_test_data() -> None:
    answer = part1("test_data.txt")
    assert 4361 == answer


def test_day1_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 539590 == answer


def test_day1_part2_test_data() -> None:
    answer = part2("test_data.txt")
    assert 467835 == answer


def test_day1_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert 69110 == answer
