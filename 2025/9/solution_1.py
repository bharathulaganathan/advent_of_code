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

# extremes = [
#     {"tile": set(), "value": tiles[0][0] + tiles[0][1]},
#     {"tile": set(), "value": - (tiles[0][0] + tiles[0][1])},
#     {"tile": set(), "value": tiles[0][1] - tiles[0][0]},
#     {"tile": set(), "value": tiles[0][0] - tiles[0][1]},
# ]

# for tile in tiles:
#     tile_extremes = [
#         tile[0] + tile[1],
#         - (tile[0] + tile[1]),
#         tile[1] - tile[0],
#         tile[0] - tile[1],
#     ]
#     for i in range(len(extremes)):
#         if tile_extremes[i] == extremes[i]["value"]:
#             extremes[i]["tile"].add(tile)
#         elif tile_extremes[i] < extremes[i]["value"]:
#             extremes[i]["tile"] = {tile}
#             extremes[i]["value"] = tile_extremes[i]

# max_area = 0
# for i in [0, 2]:
#     for j in extremes[i]["tile"]:
#         for k in extremes[i + 1]["tile"]:
#             new_area = (abs(j[0] - k[0]) + 1) * (abs(j[1] - k[1]) + 1)
#             if new_area > max_area:
#                 max_area = new_area

max_area = 0
for i in range(len(tiles)):
    for j in range(i, len(tiles)):
        new_area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (
            abs(tiles[i][1] - tiles[j][1]) + 1
        )
        if new_area > max_area:
            max_area = new_area

print(max_area)
