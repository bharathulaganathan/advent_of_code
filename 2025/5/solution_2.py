import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

fresh_range = []

with open(file_path, "r") as input:
    top = True
    for row in input:
        row = row.strip()
        if row == "":
            break
        else:
            fresh_item = row.split("-")
            fresh_range.append([int(fresh_item[0]), int(fresh_item[1])])

i = 0
while i < len(fresh_range):
    while True:
        change = False
        for j in range(i+1, len(fresh_range)):
            if ((fresh_range[i][0] >= fresh_range[j][0] and fresh_range[i][0] <= fresh_range[j][1])
                or 
                (fresh_range[i][1] >= fresh_range[j][0] and fresh_range[i][1] <= fresh_range[j][1])):
                fresh_range[i][0] = min(fresh_range[i][0], fresh_range[j][0])
                fresh_range[i][1] = max(fresh_range[i][1], fresh_range[j][1])
                del fresh_range[j]
                change = True
            if change:
                break
        if change:
            continue
        i += 1
        break

fresh_count = 0

for item in fresh_range:
    fresh_count += item[1] - item[0] + 1

print(fresh_count)