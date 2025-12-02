import copy

numbers = []

file_name = "input.txt"
with open(file_name, "r") as input:
    input = input.read()
    numbers = input.split(",")

for i in range(len(numbers)):
    numbers[i] = numbers[i].strip().split("-")
    
invalid_sum_1 = 0
invalid_sum_2 = 0

for number in numbers:
    for between in range(int(number[0]), int(number[1]) + 1):            
        between = str(between)
        half_between = int(len(between)/2)
        if between[:half_between] == between[half_between:]:
            invalid_sum_1 += int(between)
        factors = []
        for num in range(1, int(len(between)/2)+1):
            if int(len(between)) % num == 0:
                factors.append(num)
        # print(f"{between} {factors}")
        for factor in factors:
            between_copy = copy.deepcopy(between)
            pieces = []
            while len(between_copy) > 0 :
                building = ""
                for i in range(factor):
                    building += between_copy[0]
                    between_copy = between_copy[1:]
                pieces.append(building)
            # print(f"{between} {factors} {pieces}")
            invalid = True
            for i in range(1, len(pieces)):
                if pieces[0] != pieces[i]:
                    invalid = False
                    break
            if invalid:
                # print(f"{between} {factors} {pieces}")
                invalid_sum_2 += int(between)
                break

            
print("Advent of Code 2025 Day 2")
print(f"Part One: {invalid_sum_1}")
print(f"Part Two: {invalid_sum_2}")