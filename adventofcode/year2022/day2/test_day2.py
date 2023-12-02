from adventofcode.year2022.day2.solution import part1, part2


def test_day1_part1_test_data() -> None:
    answer = part1("test_data.txt")
    assert 15 == answer


def test_day1_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 14163 == answer


def test_day1_part2_test_data() -> None:
    answer = part2("test_data.txt")
    assert 12 == answer


def test_day1_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert 12091 == answer
