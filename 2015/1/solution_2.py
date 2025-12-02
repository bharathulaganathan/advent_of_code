import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

with open(file_path, "r") as input:
    directions = input.read()

floors = 0
basement_search = True
for turn in range(len(directions)):
    if directions[turn] == "(":
        floors += 1
    elif directions[turn] == ")":
        floors -= 1
    # print(f"{turn} {floors}")
    if floors == -1 and basement_search:
        basement_steps = turn + 1
        basement_search = False

print("Advent of Code 2015 Day 25")
print(f"Part One: {floors}")
print(f"Part Two: {basement_steps}")