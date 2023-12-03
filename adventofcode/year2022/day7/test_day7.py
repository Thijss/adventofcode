from adventofcode.year2022.day7.solution import part1, part2


def test_part1_test_data() -> None:
    answer = part1("test_data.txt")
    assert 95437 == answer


def test_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 1778099 == answer


def test_part2_test_data() -> None:
    answer = part2("test_data.txt")
    assert 24933642 == answer


def test_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert 1623571 == answer
