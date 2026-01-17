import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

words =[]

with open(file_path, "r") as input:
    for row in input:
        words.append(row.strip())

nice = 0

for word in words:
    pair = False
    gap = False
    for i in range(len(word) - 2):
        for j in range(i + 2, len(word) - 1):
            if word[i:i+2] == word[j:j+2]:
                pair = True
                break
        if pair:
            break
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            gap = True
            break
    if pair and gap:
        nice += 1

print(nice)