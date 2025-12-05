import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

fresh = []
check = []

with open(file_path, "r") as input:
    top = True
    for row in input:
        row = row.strip()
        if row == "":
            top = False
        elif top:
            fresh_range = row.split("-")
            fresh.append([int(fresh_range[0]), int(fresh_range[1])])
        else:
            check.append(int(row))

fresh_count = 0

for id in check:
    for items in fresh:
        if id >= items[0] and id <= items[1]:
            fresh_count += 1
            break

print(fresh_count)