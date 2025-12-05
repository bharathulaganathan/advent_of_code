num = 3113322113
process = 40

num = str(num)
for _ in range(process):
    current_num = ""
    count = 0
    new_num = ""
    for i in range(len(num)):
        if num[i] == current_num:
            count += 1
        else:
            if count > 0:
                new_num += str(count) + current_num
            current_num = num[i]
            count = 1
    new_num += str(count) + current_num
    num = new_num

print(len(num))