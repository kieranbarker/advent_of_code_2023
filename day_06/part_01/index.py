import math
from pathlib import Path
import re

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
times, distances = contents.splitlines()

_, *times = re.split(" +", times)
_, *distances = re.split(" +", distances)

possibilities_per_race = []

for index, time in enumerate(times):
    time = int(time)
    possibilities = []

    for ms in range(1, time):
        distance_traveled = ms * (time - ms)
        record_distance = int(distances[index])

        if distance_traveled > record_distance:
            possibilities.append(distance_traveled)

    number_of_possibilities = len(possibilities)
    possibilities_per_race.append(number_of_possibilities)

product = math.prod(possibilities_per_race)
print(product)
