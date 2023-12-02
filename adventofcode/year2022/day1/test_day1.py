from adventofcode.year2022.day1.solution import part1, part2


def test_day1_part1_test_data() -> None:
    answer = part1("test_data.txt")
    assert 24000 == answer


def test_day1_part1_real_data() -> None:
    answer = part1("real_data.txt")
    assert 68292 == answer


def test_day1_part2_test_data() -> None:
    answer = part2("test_data.txt")
    assert 45000 == answer


def test_day1_part2_real_data() -> None:
    answer = part2("real_data.txt")
    assert 203203 == answer
