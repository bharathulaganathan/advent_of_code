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
    highest_1s = "0"
    for i in range(len(bank)-1):
        if bank[i] > highest_10s:
            highest_10s = bank[i]
            highest_1s = bank[i+1]
        elif bank[i+1] > highest_1s:
            highest_1s = bank[i+1]
    joltage += int(highest_10s + highest_1s)

print(joltage)