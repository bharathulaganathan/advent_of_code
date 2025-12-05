num = 3113322113
process = 50

num = str(num)

def calc(num, process):
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
    return num

num = calc(num, process)

print(len(num))