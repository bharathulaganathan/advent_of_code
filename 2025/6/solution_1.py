import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

math = []
with open(file_path, "r") as input:
    for row in input:
        row = row.strip().split()
        math.append(row)

calc_index = len(math) - 1
total = 0
for i in range(len(math[calc_index])):
    if math[calc_index][i] == "+":
        sum_mult = 0
    elif math[calc_index][i] == "*":
        sum_mult = 1
    for j in range(len(math)-1):
        if math[calc_index][i] == "+":
            sum_mult += int(math[j][i])
        elif math[calc_index][i] == "*":
            sum_mult *= int(math[j][i])
    total += sum_mult

print(total)