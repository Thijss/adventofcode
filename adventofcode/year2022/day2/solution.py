from enum import IntEnum
from typing import Self

from adventofcode.lib import load_data


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __gt__(self, other: Self) -> bool:  # pyright: ignore [reportIncompatibleMethodOverride]
        if self == self.ROCK and other == other.SCISSORS:
            return True
        if self == self.PAPER and other == other.ROCK:
            return True
        if self == self.SCISSORS and other == other.PAPER:
            return True
        return False

    @classmethod
    def from_letter(cls, letter: str) -> "Shape":
        if letter in ["A", "X"]:
            return cls.ROCK
        if letter in ["B", "Y"]:
            return cls.PAPER
        if letter in ["C", "Z"]:
            return cls.SCISSORS
        raise ValueError(f"Invalid letter {letter}")

    @classmethod
    def lose(cls, other: "Shape") -> "Shape":
        if other == cls.ROCK:
            return cls.SCISSORS
        if other == cls.PAPER:
            return cls.ROCK
        return cls.PAPER

    @classmethod
    def win(cls, other: "Shape") -> "Shape":
        if other == cls.ROCK:
            return cls.PAPER
        if other == cls.PAPER:
            return cls.SCISSORS
        return cls.ROCK

    @classmethod
    def draw(cls, other: "Shape") -> "Shape":
        return other


def part1(file_name: str) -> int:
    data = load_data(year=2022, day=2, file_name=file_name)

    data = data.split("\n")
    games: list[tuple[Shape, Shape]] = [(Shape.from_letter(line[0]), Shape.from_letter(line[-1])) for line in data]
    return _calculate_scores(games)


def part2(file_name: str) -> int:
    data = load_data(year=2022, day=2, file_name=file_name)

    data = data.split("\n")
    game_plans = [(Shape.from_letter(line[0]), line[-1]) for line in data]

    games: list[tuple[Shape, Shape]] = []
    for opponent, outcome in game_plans:
        if outcome == "X":
            games.append((opponent, Shape.lose(opponent)))
        elif outcome == "Y":
            games.append((opponent, Shape.draw(opponent)))
        else:
            games.append((opponent, Shape.win(opponent)))

    return _calculate_scores(games)


def _calculate_scores(games: list[tuple[Shape, Shape]]) -> int:
    score = 0
    for game in games:
        your_shape, my_shape = game
        match_score = _calculate_match_score(your_shape, my_shape)
        score += match_score + my_shape
    return score


def _calculate_match_score(your_shape: Shape, my_shape: Shape) -> int:
    if my_shape > your_shape:
        return 6
    if my_shape == your_shape:
        return 3
    return 0
