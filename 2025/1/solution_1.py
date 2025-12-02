import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

rotations = []

with open(file_path, "r") as input:
    for row in input:
        rotations.append(row.strip())

dial = 50
stop = 0

for rotation in rotations:
    change = int(rotation[1:])
    if rotation[0] == "R":
        dial = (dial + change) % 100
    else:
        dial = abs((dial - change) % 100)
    if dial == 0:
        stop += 1

print(stop)