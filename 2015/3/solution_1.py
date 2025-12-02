import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

with open(file_path, "r") as input:
    directions = input.read()
    # print(directions)

houses = set()
row = 0
col = 0
houses.add((row, col))
for move in directions:
    if move == "^":
        row += 1
    elif move == "v":
        row -= 1
    elif move == ">":
        col += 1
    elif move == "<":
        col -= 1
    houses.add((row, col))

print("Advent of Code 2015 Day 3")
print(f"Part One: {len(houses)}")
# print(f"Part Two: {}")