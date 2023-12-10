from pathlib import Path

path = Path(__file__).parents[1] / "sample.txt"
contents = path.read_text()
lines = contents.splitlines()
lines = [[int(n) for n in line.split(" ")] for line in lines]


def get_differences(line: list[int]) -> list[int]:
    differences = []
    line_length = len(line)

    for i in range(line_length):
        j = i + 1

        if j < line_length:
            diff = abs(line[i] - line[j])
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
            sequences[i][j].append(0)
        else:
            x = sequences[i][j][-1] + sequences[i][j - 1][-1]
            sequences[i][j].append(x)

total = 0

for sequence in sequences:
    total += sequence[-1][-1]

print(total)  # Works for the sample input but not the actual input :')
