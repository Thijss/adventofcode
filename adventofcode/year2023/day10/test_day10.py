from adventofcode.year2023.day10.solution import part1, part2


def test_part1a_test_data() -> None:
    answer = part1("test_data_part1a.txt")
    assert 4 == answer


def test_part1b_test_data() -> None:
    answer = part1("test_data_part1b.txt")
    assert 8 == answer


def test_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 6768 == answer


def test_part2a_test_data() -> None:
    answer = part2("test_data_part2a.txt")
    assert 4 == answer


def test_part2b_test_data() -> None:
    answer = part2("test_data_part2b.txt")
    assert 4 == answer


def test_part2c_test_data() -> None:
    answer = part2("test_data_part2c.txt")
    assert 8 == answer


def test_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert 351 == answer
