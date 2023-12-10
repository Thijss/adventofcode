from adventofcode.year2023.day10.solution import part1


def test_part1a_test_data() -> None:
    answer = part1("test_data_part1a.txt")
    assert 4 == answer


def test_part1b_test_data() -> None:
    answer = part1("test_data_part1b.txt")
    assert 8 == answer


def test_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 6768 == answer


def test_part2_test_data() -> None:
    answer = part2("test_data.txt")
    assert 5905 == answer


def test_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert 252137472 == answer
