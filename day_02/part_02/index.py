from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
lines = contents.splitlines()

powers = []

for line in lines:
    _, cubes = line.split(": ")

    rounds = cubes.split("; ")
    cube_count = {"red": [], "green": [], "blue": []}

    for round in rounds:
        cubes_revealed = round.split(", ")

        for cube in cubes_revealed:
            quantity, color = cube.split(" ")
            quantity = int(quantity)
            cube_count[color].append(quantity)

    min_red = max(cube_count["red"])
    min_blue = max(cube_count["blue"])
    min_green = max(cube_count["green"])

    powers.append(min_red * min_blue * min_green)

sum_of_powers = sum(powers)
print(sum_of_powers)
