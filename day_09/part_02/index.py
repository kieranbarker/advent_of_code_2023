from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
lines = contents.splitlines()
lines = [[int(n) for n in line.split(" ")] for line in lines]


def get_differences(line: list[int]) -> list[int]:
    differences = []
    line_length = len(line)

    for i in range(line_length):
        j = i + 1

        if j < line_length:
            diff = line[j] - line[i]
            differences.append(diff)

    return differences


sequences = [[line] for line in lines]

for i, arr in enumerate(lines):
    differences = get_differences(arr)
    sequences[i].append(differences)
    all_zero = all(diff == 0 for diff in differences)

    while not all_zero:
        differences = get_differences(differences)
        sequences[i].append(differences)
        all_zero = all(diff == 0 for diff in differences)

for i in range(len(sequences)):
    sequences[i].reverse()

    for j in range(len(sequences[i])):
        if j == 0:
            sequences[i][j].insert(0, 0)
        else:
            x = sequences[i][j][0] - sequences[i][j - 1][0]
            sequences[i][j].insert(0, x)

total = 0

for sequence in sequences:
    total += sequence[-1][0]

print(total)
