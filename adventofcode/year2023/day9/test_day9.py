from adventofcode.year2023.day9.solution import part1, part2


def test_part1_test_data() -> None:
    answer = part1("test_data.txt")
    assert 114 == answer


def test_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 1681758908 == answer


def test_part2_test_data() -> None:
    answer = part2("test_data.txt")
    assert -1 == answer


def test_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert -1 == answer
