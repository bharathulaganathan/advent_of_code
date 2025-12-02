import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

rotations = []

with open(file_path, "r") as input:
    for line in input:
        rotations.append(line.strip())

dial = 50
pass_0 = 0

for rotation in rotations:
    change = int(rotation[1:])
    if rotation[0] == "R":
        new_dial = (dial + change)
    else:
        new_dial = (dial - change)
    if dial > new_dial:
        small = new_dial
        large = dial
    else:
        small = dial + 1
        large = new_dial + 1
    for click in range(small,large):
        if (click % 100) == 0:
            pass_0 += 1
    dial = new_dial % 100

print(pass_0)