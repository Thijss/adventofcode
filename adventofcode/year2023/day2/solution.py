from adventofcode.lib import load_data

_ELF_BAG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}



def part1(file_name: str) -> int:
    data = load_data(year=2023, day=2, file_name=file_name)
    data = data.replace(";", ",")
    games = data.split("\n")
    game_ids: list[int] = []
    for game in games:
        game_id, draws = _parse_game(game)
        for draw in draws:
            count, color = draw
            if count > _ELF_BAG[color]:
                break
        else:
            game_ids.append(game_id)
    return sum(game_ids)


def part2(file_name: str) -> int:
    data = load_data(year=2023, day=2, file_name=file_name)
    data = data.replace(";", ",")
    games = data.split("\n")
    powers: list[int] = []

    for game in games:
        _, draws = _parse_game(game)
        max_red, max_green, max_blue = 0, 0, 0

        for draw in draws:
            count, color = draw
            if color == "red":
                max_red = max(max_red, count)
            elif color == "green":
                max_green = max(max_green, count)
            elif color == "blue":
                max_blue = max(max_blue, count)
        powers.append(max_red * max_green * max_blue)
    return sum(powers)


def _parse_game(game: str) -> tuple[int, list[tuple[int, str]]]:
    game_id, draws = game.split(": ")
    game_id = int(game_id.replace("Game ", ""))
    draws = draws.split(", ")
    draws = [(int(count), color)  for count, color in [draw.split(" ") for draw in draws]]
    return game_id, draws