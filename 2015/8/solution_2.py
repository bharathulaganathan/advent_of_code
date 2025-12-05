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
    if text[i] == "\\":
        if text[i+1] == "x":
            total += 1
            i += 4
        else:
            total += 2
            i += 2
    elif text[i] == "\"":
        total += 2
        i += 1
    else:
        i += 1

print(total)