import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

banks = []
with open(file_path, "r") as input:
    for row in input:
        banks.append(row.strip())

joltage = 0

for bank in banks:
    highest_10s = "0"
    highest_index = "0"
    for i in range(len(bank)-1):
        if bank[i] > highest_10s:
            highest_10s = bank[i]
            highest_index = i
    highest_1s = "0"
    for j in range(int(highest_index+1), len(bank)):
        if bank[j] > highest_1s:
            highest_1s = bank[j]
    joltage += int(highest_10s + highest_1s)

print(joltage)