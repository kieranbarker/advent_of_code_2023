import re
from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
lines = contents.splitlines()

card_points = []

for line in lines:
    _, numbers = re.split(": +", line)
    winning_numbers, our_numbers = re.split(" \| +", numbers)

    winning_numbers = re.split(" +", winning_numbers)
    our_numbers = re.split(" +", our_numbers)

    number_of_matches = 0

    for number in our_numbers:
        if number in winning_numbers:
            number_of_matches += 1

    if number_of_matches > 0:
        # We subtract 1 because the power is the number of times we want to
        # double the value. E.g. if we had 1,4,2,8, the number of matches would
        # be 4 while the number of doubles would be 3.
        points = 2 ** (number_of_matches - 1)
        card_points.append(points)

sum_of_points = sum(card_points)
print(sum_of_points)
