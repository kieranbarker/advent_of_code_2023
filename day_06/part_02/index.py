from pathlib import Path
import re

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
time, distance = contents.splitlines()

time = re.split(" +", time)[1:]
time = int("".join(time))

distance = re.split(" +", distance)[1:]
distance = int("".join(distance))

possibilities = []

for ms in range(1, time):
    distance_traveled = ms * (time - ms)

    if distance_traveled > distance:
        possibilities.append(distance_traveled)

number_of_possibilities = len(possibilities)
print(number_of_possibilities)
