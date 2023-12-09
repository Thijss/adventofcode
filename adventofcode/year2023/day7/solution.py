from collections import Counter
from enum import IntEnum, auto
from typing import Self

from adventofcode.lib import load_data

_CARD_TO_VALUE = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=7, file_name=file_name)

    hands = [_Hand(line, jokers=False) for line in data.splitlines()]
    hands.sort()

    total = 0
    for idx, hand in enumerate(hands):
        total += hand.bet * (idx + 1)
    return total


def part2(file_name: str) -> int:
    data = load_data(year=2023, day=7, file_name=file_name)

    hands = [_Hand(line, jokers=True) for line in data.splitlines()]
    hands.sort()

    total = 0
    for idx, hand in enumerate(hands):
        total += hand.bet * (idx + 1)
    return total


class _Type(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()

    @classmethod
    def from_string(cls, hand: str):
        counter_list = list(Counter(hand).values())
        counter_list.sort(reverse=True)
        if counter_list == [5]:
            return cls.FIVE_OF_A_KIND
        if counter_list == [4, 1]:
            return cls.FOUR_OF_A_KIND
        if counter_list == [3, 2]:
            return cls.FULL_HOUSE
        if counter_list == [3, 1, 1]:
            return cls.THREE_OF_A_KIND
        if counter_list == [2, 2, 1]:
            return cls.TWO_PAIR
        if counter_list == [2, 1, 1, 1]:
            return cls.ONE_PAIR
        return cls.HIGH_CARD

    def apply_jokers(self, jokers: int):
        if jokers == 0:
            return self
        if self in [self.FIVE_OF_A_KIND, self.FOUR_OF_A_KIND, self.FULL_HOUSE]:
            return self.FIVE_OF_A_KIND
        if self is self.THREE_OF_A_KIND:
            return self.FOUR_OF_A_KIND
        if self is self.TWO_PAIR and jokers == 1:
            return self.FULL_HOUSE
        if self is self.TWO_PAIR and jokers == 2:
            return self.FOUR_OF_A_KIND
        if self is self.ONE_PAIR:
            return self.THREE_OF_A_KIND
        return self.ONE_PAIR


class _Hand:
    def __init__(self, data: str, jokers: bool) -> None:
        self.hand = data.split(" ")[0]
        self.bet = int(data.split(" ")[1])
        self.jokers = jokers

    def __eq__(self: Self, other: Self) -> bool:  # pyright: ignore [reportIncompatibleMethodOverride]
        return self.hand == other.hand

    def __gt__(self, other: Self) -> bool:  # pyright: ignore [reportIncompatibleMethodOverride]
        if self.hand == other.hand:
            return False
        if self.type != other.type:
            return self.type > other.type

        mapping = _CARD_TO_VALUE.copy()
        if self.jokers:
            mapping["J"] = 1

        for index in range(len(self.hand)):
            if self.hand[index] == other.hand[index]:
                continue
            char1 = self.hand[index]
            char2 = other.hand[index]

            if char1 in mapping:
                char1 = mapping[char1]
            if char2 in mapping:
                char2 = mapping[char2]

            return int(char1) > int(char2)
        raise ValueError("Invalid hand")

    @property
    def type(self) -> _Type:
        hand_type = _Type.from_string(self.hand)
        if self.jokers:
            j_count = Counter(self.hand)["J"]
            return hand_type.apply_jokers(j_count)
        return _Type.from_string(self.hand)

    def __str__(self) -> str:
        return self.hand

    def __repr__(self) -> str:
        return f"_Hand('{self.hand}') - {self.type.name}"
