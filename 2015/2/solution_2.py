import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

dimensions = []
with open(file_path, "r") as input:
    for row in input:
        dimensions.append(row.strip())

print(dimensions)

wrapping = 0
ribbon = 0

for dimension in dimensions:
    dimension = dimension.split("x")
    for dim in range(len(dimension)):
        dimension[dim] = int(dimension[dim])
    dimension.sort()
    print(dimension)
    wrapping += 2*(1.5*(dimension[0]*dimension[1]) + dimension[1]*dimension[2] + dimension[2]*dimension[0])
    ribbon += 2*(dimension[0]+dimension[1]) + dimension[0]*dimension[1]*dimension[2]
    
    
print("Advent of Code 2015 Day 2")
print(f"Part One: {int(wrapping)}")
print(f"Part Two: {ribbon}")