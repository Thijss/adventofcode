from adventofcode.lib import load_data

_COMPATIBLE_DIRECTION: dict[str, list[str]] = {
    "left": ["-", "F", "L"],
    "right": ["-", "7", "⅃"],
    "top": ["|", "7", "F"],
    "bottom": ["|", "L", "⅃"],
}


_MODIFIERS: dict[str, tuple[int, int]] = {
    "left": (0, -1),
    "right": (0, 1),
    "top": (-1, 0),
    "bottom": (1, 0),
}

_CHAR_TO_DIRECTION: dict[str, tuple[str, ...]] = {
    "S": ("left", "right", "top", "bottom"),
    "|": ("top", "bottom"),
    "-": ("left", "right"),
    "F": ("right", "bottom"),
    "L": ("right", "top"),
    "7": ("left", "bottom"),
    "⅃": ("left", "top"),
}


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=10, file_name=file_name)
    data = data.replace("J", "⅃")
    grid = Grid(data)
    print(data)
    grid.walk(0)
    grid.walk(1)

    return max(grid.distances.values())


class Grid:
    def __init__(self, data: str) -> None:
        self.data = {idx: line for idx, line in enumerate(data.splitlines())}
        self.start_point = self._get_start_point(data, len(self.data[0]))
        self.location = self.start_point
        self.distances: dict[tuple[int, int], int] = {self.location: 0}

    @property
    def row(self) -> int:
        return self.location[0]

    @property
    def col(self) -> int:
        return self.location[1]

    def walk(self, start_idx: int) -> None:
        steps = 0
        self.location = self.start_point
        self.history = {self.start_point}
        start_neighbours = self.find_neighbours()
        self.location = start_neighbours[start_idx]

        while True:
            steps += 1
            if self.location in self.distances:
                self.distances[self.location] = min(self.distances[self.location], steps)
            else:
                self.distances[self.location] = steps

            self.history.add(self.location)

            neighbours = self.find_neighbours()
            if not neighbours:
                break
            if len(neighbours) > 1:
                print()
            self.location = neighbours[0]

    def find_directions(self) -> tuple[str, ...]:
        current_char = self.data[self.row][self.col]
        return _CHAR_TO_DIRECTION[current_char]

    def find_neighbours(self) -> list[tuple[int, int]]:
        neighbours: list[tuple[int, int]] = list()
        for direction in self.find_directions():
            r_mod, c_mod = _MODIFIERS[direction]
            row, col = self.row + r_mod, self.col + c_mod

            if (row, col) in self.history:
                continue

            if not self.is_within_limit(row, col):
                continue
            char = self.data[row][col]
            if char in _COMPATIBLE_DIRECTION[direction]:
                neighbours.append((row, col))

        return neighbours

    def is_within_limit(self, row: int, col: int) -> bool:
        n_rows, n_cols = len(self.data), len(self.data[0])
        return row >= 0 and row < n_rows and col >= 0 and col < n_cols

    def _get_start_point(self, data: str, row_length: int) -> tuple[int, int]:
        s_row = data.find("S") // (row_length + 1)
        s_col = data.find("S") % (row_length + 1)
        return s_row, s_col

    def get_surrounding(self, row: int, col: int) -> str:
        top_row = self.data[row - 1][col - 1 : col + 2] if row > 0 else "___"
        mid_row = self.data[row][col - 1 : col + 2]
        bot_row = self.data[row + 1][col - 1 : col + 2] if row < len(self.data) - 1 else "___"
        return top_row + "\n" + mid_row + "\n" + bot_row
