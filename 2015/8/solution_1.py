import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

text = ""

with open(file_path, "r") as input:
    for row in input:
        row = row.strip()
        text += row

total = 0
i = 0
while i < len(text):
    if text[i] == "\"":
        total += 1
        i += 1
    elif text[i] == "\\":
        if text[i+1] == "x":
            total += 3
            i += 4
        else:
            total += 1
            i += 2
    else:
        i += 1

print(total)