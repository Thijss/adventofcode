from pathlib import Path

_ROOT_DIR = Path(__file__).parent


def load_data(year: int, day: int, file_name: str) -> str:
    path = _ROOT_DIR / f"year{year}" / f"day{day}" / "input" / file_name
    with open(path) as f:
        return f.read()
