import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

tachyon = []
with open(file_path, "r") as input:
    for row in input:
        tachyon.append(row.strip())

beams = []

for i in range(len(tachyon[0])):
    if tachyon[0][i] == "S":
        beams.append(1)
    else:
        beams.append(0)

for i in range(2, len(tachyon), 2):
    for j in range(len(tachyon[i])):
        if tachyon[i][j] == "^":
            beams[j - 1] += beams[j]
            beams[j + 1] += beams[j]
            beams[j] = 0

print(sum(beams))
