from adventofcode.year2023.day7.solution import part1, part2


def test_part1_test_data() -> None:
    answer = part1("test_data.txt")
    assert 288 == answer


def test_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 252000 == answer


def test_part2_test_data() -> None:
    answer = part2("test_data.txt")
    assert 71503 == answer


def test_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert 36992486 == answer
