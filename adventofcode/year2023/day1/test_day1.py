from adventofcode.year2023.day1.solution import part1, part2


def test_day1_part1_test_data():
    answer = part1("test_data_part1.txt")
    assert 142 == answer


def test_day1_part1_real_data():
    answer = part1("real_data.txt")
    assert 53194 == answer


def test_day1_part2_test_data():
    answer = part2("test_data_part2.txt")
    assert 281 == answer


def test_day1_part2_real_data():
    answer = part2("real_data.txt")
    assert 54249 == answer
