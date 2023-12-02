from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
lines = contents.splitlines()

bag = {"red": 12, "green": 13, "blue": 14}
possible_game_ids = []

for line in lines:
    game, cubes = line.split(": ")

    game_id = game.removeprefix("Game ")
    game_id = int(game_id)

    rounds = cubes.split("; ")
    is_possible_game = True

    for round in rounds:
        cubes_revealed = round.split(", ")

        for cube in cubes_revealed:
            quantity, color = cube.split(" ")
            quantity = int(quantity)

            if quantity > bag[color]:
                is_possible_game = False
                break

    if is_possible_game:
        possible_game_ids.append(game_id)

sum_of_ids = sum(possible_game_ids)
print(sum_of_ids)
