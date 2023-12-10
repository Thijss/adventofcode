from collections import Counter

from adventofcode.lib import load_data

_COMPATIBLE_DIRECTION: dict[str, list[str]] = {
    "left": ["━", "┏", "┗"],
    "right": ["━", "┓", "┛"],
    "top": ["┃", "┓", "┏"],
    "bottom": ["┃", "┗", "┛"],
}


_MODIFIERS: dict[str, tuple[int, int]] = {
    "left": (0, -1),
    "right": (0, 1),
    "top": (-1, 0),
    "bottom": (1, 0),
}

_CHAR_TO_DIRECTION: dict[str, tuple[str, ...]] = {
    "S": ("left", "right", "top", "bottom"),
    "┃": ("top", "bottom"),
    "━": ("left", "right"),
    "┏": ("right", "bottom"),
    "┗": ("right", "top"),
    "┓": ("left", "bottom"),
    "┛": ("left", "top"),
}


def part1(file_name: str) -> int:
    data = load_data(year=2023, day=10, file_name=file_name)
    data = (
        data.replace("-", "━").replace("|", "┃").replace("7", "┓").replace("F", "┏").replace("L", "┗").replace("J", "┛")
    )
    grid = Grid(data)
    grid.walk(0)
    grid.walk(1)
    return max(grid.distances.values())


def part2(file_name: str) -> int:
    data = load_data(year=2023, day=10, file_name=file_name)
    data = (
        data.replace("-", "━").replace("|", "┃").replace("7", "┓").replace("F", "┏").replace("L", "┗").replace("J", "┛")
    )
    grid = Grid(data)
    grid.walk(0)
    grid.mark_ground()
    grid.walk(0, search_dots=True)

    grid.history = set()
    for loc in grid.marked_dots:
        grid.spread_marks(loc, ".")

    grid.mark_locations(grid.marked_dots, "I")

    data_str = "".join(grid.data.values())
    counter = Counter(data_str)
    return min(counter["."], counter["I"])


class Grid:
    def __init__(self, data: str) -> None:
        self.data = {idx: line for idx, line in enumerate(data.splitlines())}
        self.start_point = self._get_start_point(data, len(self.data[0]))
        self.location = self.start_point
        self.distances: dict[tuple[int, int], int] = {self.location: 0}
        self.path: list[tuple[int, int]] = [self.location]
        self.marked_dots: list[tuple[int, int]] = []

    @property
    def row(self) -> int:
        return self.location[0]

    @property
    def col(self) -> int:
        return self.location[1]

    def walk(self, start_idx: int, search_dots: bool = False) -> None:
        steps = 0
        self.location = self.start_point
        self.history = {self.start_point}
        start_neighbours = list(self.find_neighbours().values())
        self.location = start_neighbours[start_idx]

        while True:
            steps += 1
            if self.location in self.distances:
                self.distances[self.location] = min(self.distances[self.location], steps)
            else:
                self.distances[self.location] = steps

            self.history.add(self.location)
            self.path.append(self.location)

            neighbours = self.find_neighbours()
            if not neighbours:
                break
            direction, self.location = list(neighbours.items())[0]
            if search_dots:
                self.search_for_dots_on_1_side(self.location, direction)

    def find_directions(self) -> tuple[str, ...]:
        current_char = self.data[self.row][self.col]
        return _CHAR_TO_DIRECTION[current_char]

    def find_neighbours(self) -> dict[str, tuple[int, int]]:
        neighbours: dict[str, tuple[int, int]] = {}
        for direction in self.find_directions():
            r_mod, c_mod = _MODIFIERS[direction]
            row, col = self.row + r_mod, self.col + c_mod

            if (row, col) in self.history:
                continue

            if not self.is_within_limit(row, col):
                continue
            char = self.data[row][col]
            if char in _COMPATIBLE_DIRECTION[direction]:
                neighbours[direction] = (row, col)

        return neighbours

    def search_for_dots_on_1_side(self, location: tuple[int, int], direction: str) -> None:
        char = self.get_point(*location)
        row, col = location
        if char == "┃":
            if direction == "bottom":
                search_location = (row, col + 1)
            elif direction == "top":
                search_location = (row, col - 1)
            else:
                return
            self.search_ldot(search_location)

        elif char == "━":
            if direction == "right":
                search_location = (row - 1, col)
            elif direction == "left":
                search_location = (row + 1, col)
            else:
                return
            self.search_ldot(search_location)
        elif char == "┏" and direction == "top":
            search_locations = (row, col - 1), (row - 1, col - 1), (row - 1, col)
            for search_location in search_locations:
                self.search_ldot(search_location)
        elif char == "┗" and direction == "left":
            search_locations = (row, col - 1), (row + 1, col - 1), (row + 1, col)
            for search_location in search_locations:
                self.search_ldot(search_location)
        elif char == "┓" and direction == "right":
            search_locations = (row, col + 1), (row - 1, col + 1), (row - 1, col)
            for search_location in search_locations:
                self.search_ldot(search_location)
        elif char == "┛" and direction == "bottom":
            search_locations = (row, col + 1), (row + 1, col + 1), (row + 1, col)
            for search_location in search_locations:
                self.search_ldot(search_location)

    def mark_locations(self, locations: list[tuple[int, int]], char: str) -> None:
        for location in locations:
            self.mark_location(location, char)

    def mark_location(self, location: tuple[int, int], char: str) -> None:
        row, col = location
        row_list = list(self.data[row])
        row_list[col] = char
        self.data[row] = "".join(row_list)

    def search_ldot(self, search_location: tuple[int, int]) -> None:
        if search_location in self.marked_dots:
            return
        if not self.is_within_limit(*search_location):
            return
        search_char = self.get_point(*search_location)
        if search_char == ".":
            self.marked_dots.append(search_location)

    def spread_marks(self, location: tuple[int, int], matching_char: str) -> list[tuple[int, int]]:
        current_row, current_col = location

        neighbours: list[tuple[int, int]] = list()
        for direction in ("left", "right", "top", "bottom"):
            r_mod, c_mod = _MODIFIERS[direction]
            row, col = current_row + r_mod, current_col + c_mod

            if (row, col) in self.history or not self.is_within_limit(row, col):
                continue
            char = self.data[row][col]
            if char == matching_char:
                neighbours.append((row, col))
                self.history.add((row, col))
                self.marked_dots.append((row, col))

        for neighbour in neighbours:
            self.spread_marks(neighbour, matching_char)
        return neighbours

    def is_within_limit(self, row: int, col: int) -> bool:
        n_rows, n_cols = len(self.data), len(self.data[0])
        return row >= 0 and row < n_rows and col >= 0 and col < n_cols

    def _get_start_point(self, data: str, row_length: int) -> tuple[int, int]:
        s_row = data.find("S") // (row_length + 1)
        s_col = data.find("S") % (row_length + 1)
        return s_row, s_col

    def mark_ground(self) -> None:
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                if (row, col) not in self.history:
                    row_list = list(self.data[row])
                    row_list[col] = "."
                    self.data[row] = "".join(row_list)

    def get_point(self, row: int, col: int) -> str:
        return self.data[row][col]

    def __str__(self) -> str:
        return "\n" + "\n".join(self.data.values())
