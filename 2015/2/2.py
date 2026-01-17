import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

dimensions = []
with open(file_path, "r") as input:
    for row in input:
        dimensions.append(row.strip())

ribbon = 0

for dimension in dimensions:
    dimension = dimension.split("x")
    for dim in range(len(dimension)):
        dimension[dim] = int(dimension[dim])
    dimension.sort()
    ribbon += 2*(dimension[0]+dimension[1]) + dimension[0]*dimension[1]*dimension[2]

print(ribbon)