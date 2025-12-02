numbers = []

file_name = "input.txt"
with open(file_name, "r") as input:
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
            
print("Advent of Code 2025 Day 2")
print(f"Part One: {invalid_sum}")