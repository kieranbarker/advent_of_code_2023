from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
sequence = path.read_text().split(",")


def hash(str: str) -> int:
    current_value = 0

    for code in str.encode("ascii"):
        current_value += code
        current_value *= 17
        current_value %= 256

    return current_value


results = [hash(step) for step in sequence]
total = sum(results)
print(total)
