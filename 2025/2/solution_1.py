import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

numbers = []

with open(file_path, "r") as input:
    input = input.read()
    numbers = input.split(",")

for i in range(len(numbers)):
    numbers[i] = numbers[i].strip().split("-")
    
invalid_sum = 0

for number in numbers:
    for between in range(int(number[0]), int(number[1]) + 1):
        between = str(between)
        half_between = int(len(between)/2)
        if between[:half_between] == between[half_between:]:
            invalid_sum += int(between)

print(invalid_sum)