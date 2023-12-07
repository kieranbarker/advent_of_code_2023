import re
from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
lines = contents.splitlines()

card_points = []

for line in lines:
    numbers = re.split(": +", line)[1]
    winning_numbers, our_numbers = re.split(" \| +", numbers)

    winning_numbers = re.split(" +", winning_numbers)
    our_numbers = re.split(" +", our_numbers)

    number_of_matches = 0

    for number in our_numbers:
        if number in winning_numbers:
            number_of_matches += 1

    if number_of_matches > 0:
        number_of_doubles = number_of_matches - 1
        points = 2**number_of_doubles
        card_points.append(points)

sum_of_points = sum(card_points)
print(sum_of_points)
