import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

with open(file_path, "r") as input:
    directions = input.read()

floors = 0
for direction in directions:
    if direction == "(":
        floors += 1
    elif direction == ")":
        floors -= 1

print("Advent of Code 2015 Day 25")
print(f"Part One: {floors}")