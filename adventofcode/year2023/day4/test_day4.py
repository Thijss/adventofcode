from adventofcode.year2023.day4.solution import part1, part2


def test_part1_test_data() -> None:
    answer = part1("test_data.txt")
    assert 13 == answer


def test_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 18653 == answer


def test_part2_test_data() -> None:
    answer = part2("test_data.txt")
    assert 30 == answer


def test_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert 5921508 == answer
