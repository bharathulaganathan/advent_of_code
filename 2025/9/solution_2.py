import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

tiles = []
with open(file_path, "r") as input:
    for row in input:
        x, y = row.strip().split(",")
        x = int(x) - 1
        y = int(y) - 1
        tiles.append((x, y))

max_area = 0
for i in range(len(tiles)):
    for j in range(i, len(tiles)):
        if (tiles[i][0] == tiles[j][0]) or (tiles[i][1] == tiles[j][1]):
            area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (
                abs(tiles[i][1] - tiles[j][1]) + 1
            )

print(max_area)
