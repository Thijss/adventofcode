from adventofcode.year2023.day8.solution import part1, part2


def test_part1_test_data() -> None:
    answer = part1("test_data_part1.txt")
    assert 6 == answer


def test_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 18827 == answer


def test_part2_test_data() -> None:
    answer = part2("test_data_part2.txt")
    assert 6 == answer


def test_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert 20220305520997 == answer
