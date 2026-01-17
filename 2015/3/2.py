import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

with open(file_path, "r") as input:
    directions = input.read()

houses = set()
santa_row = 0
santa_col = 0
robo_row = 0
robo_col = 0
houses.add((0, 0))

def move(row, col, direction):
    if direction == "^":
        row += 1
    elif direction == "v":
        row -= 1
    elif direction == ">":
        col += 1
    elif direction == "<":
        col -= 1
    return (row, col)

while len(directions) > 0:
    santa_row, santa_col = move(santa_row, santa_col, directions[0])
    houses.add((santa_row, santa_col))
    directions = directions[1:]
    if len(directions) > 0:
        robo_row, robo_col = move(robo_row, robo_col, directions[0])
        houses.add((robo_row, robo_col))
        directions = directions[1:]

print(len(houses))