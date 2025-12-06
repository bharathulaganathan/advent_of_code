import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

nums = []
with open(file_path, "r") as input:
    for row in input:
        row = row.strip("\n")
        nums.append(row)
calcs = nums.pop()

def eval(start, end, nums, calc):
    to_eval = []
    for i in range(start, end):
        num = ""
        for j in range(len(nums)):
            num += nums[j][i]
        to_eval.append(int(num))
    if calc == "+":
        return to_sum(to_eval)
    elif calc == "*":
        return to_mult(to_eval)

def to_sum(nums):
    sumed = 0
    for num in nums:
        sumed += num
    return sumed

def to_mult(nums):
    multed = 1
    for num in nums:
        multed *= num
    return multed

total = 0
num_end = len(calcs) + 1
for i in range(len(calcs)-1,-1,-1):
    if calcs[i] != " ":
        total += eval(i, num_end - 1, nums, calcs[i])
        num_end = i

print(total)