import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

banks = []
with open(file_path, "r") as input:
    for row in input:
        banks.append(row.strip())

battery_len = 12
joltage = 0

for bank in banks:
    power = ""
    rotation = len(bank) - battery_len + 1
    while len(power) < battery_len:
        highest = "0"
        highest_index = 0
        for i in range(rotation):
            if bank[i] > highest:
                highest = bank[i]
                highest_index = i
        power += bank[highest_index]
        bank = bank[highest_index+1:]
        rotation -= highest_index
    joltage += int(power)

print(joltage)