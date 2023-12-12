from pathlib import Path

path = Path(__file__).parents[1] / "sample.txt"
contents = path.read_text()
pipes = [list(line) for line in contents.splitlines()]

# Find the starting position of the animal.
for i, row in enumerate(pipes):
    try:
        row, col = i, row.index("S")
        break
    except ValueError:
        continue


# Traverse the loop...
current_position = pipes[row][col]

up = None if row - 1 == -1 else pipes[row - 1][col]
print(up)  # "."

right = None if col + 1 == len(pipes[row]) else pipes[row][col + 1]
print(right)  # "J"

down = None if row + 1 == len(pipes) else pipes[row + 1][col]
print(down)  # "|"

left = None if col - 1 == -1 else pipes[row][col - 1]
print(left)  # None

# Does this mean the two connected pipes must be to the right and bottom?
