import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

room = []

with open(file_path, "r") as input:
    for row in input:
        room.append((row.strip()))

rolls = 0

for i in range(len(room)):
    for j in range(len(room[i])):
        if room[i][j] != "@":
            continue
        x_min = max(i - 1, 0)
        x_max = min(i + 1, len(room)-1)
        y_min = max(j - 1, 0)
        y_max = min(j + 1, len(room[i])-1)
        papers = 0
        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max+1):
                if room[x][y] == "@" and not(x == i and y == j):
                    papers += 1
        if papers < 4:
            rolls += 1

print(rolls)