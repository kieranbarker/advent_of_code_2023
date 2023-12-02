from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
lines = contents.splitlines()

calibration_values = []

for line in lines:
    digits = [char for char in line if char.isdigit()]
    calibration_value = int(digits[0] + digits[-1])
    calibration_values.append(calibration_value)

sum_of_values = sum(calibration_values)
print(sum_of_values)
