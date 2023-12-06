from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
seed_numbers, *maps = contents.split("\n\n")

seed_numbers = seed_numbers.removeprefix("seeds: ").split(" ")
seed_numbers = [int(seed) for seed in seed_numbers]
maps = [map.split("\n") for map in maps]

conversions = {}

for name, *rows in maps:
    name = name.removesuffix(" map:")
    conversions[name] = []

    for row in rows:
        range_pair = []

        values = [int(value) for value in row.split(" ")]
        dest_range_start, src_range_start, range_length = values

        src_range_stop = src_range_start + range_length + 1
        src_range = range(src_range_start, src_range_stop)
        range_pair.append(src_range)

        dest_range_stop = dest_range_start + range_length + 1
        dest_range = range(dest_range_start, dest_range_stop)
        range_pair.append(dest_range)

        conversions[name].append(range_pair)


def convert_number(number: int, conversion: str) -> int:
    converted_number = number

    for src_range, dest_range in conversions[conversion]:
        if number in src_range:
            index = number - src_range.start
            converted_number = dest_range[index]
            break

    return converted_number


location_numbers = []

for seed_number in seed_numbers:
    converted_number = seed_number

    for conversion in conversions.keys():
        converted_number = convert_number(converted_number, conversion)

    location_numbers.append(converted_number)

min_location_number = min(location_numbers)
print(min_location_number)
