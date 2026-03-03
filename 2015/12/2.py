import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = "input" + ".txt"
file_path = os.path.join(base_dir, input_file)

docs = []
with open(file_path, "r") as input:
    for row in input:
        row = row.strip()
        docs.append(row)


def main():
    for doc in docs:
        str_data = doc
        c = 0
        nums = set()
        while c < len(str_data):
            c, num = get_num(c, str_data)
            if num is not None:
                nums.add((c,num))
            c = get_red(c, str_data, nums)
            c += 1
        total = 0
        for n in nums:
            total += n[1]
        print(total)


def get_num(c, str_data):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if str_data[c] not in nums:
        return c, None
    num = str_data[c]
    if str_data[c-1] == "-":
        num = "-" + num
    c += 1
    while c < len(str_data):
        if str_data[c] in nums:
            num = num + str_data[c]
            c += 1
        else:
            break
    return c-1, int(num)

def get_red(c, str_data, nums):
    red = c
    if not str_data[c : c + 6] == ':"red"':
        return c
    bracket = 1
    while c >= 0:
        if str_data[c] == "{":
            bracket -= 1
        elif str_data[c] == "}":
            bracket += 1
        if bracket == 0:
            break
        c -= 1
    sub = 0
    while c < len(str_data):
        if c < red:
            c, num = get_num(c, str_data)
            if num is not None:
                nums.discard((c,num))
        if str_data[c] == "{":
            bracket += 1
        elif str_data[c] == "}":
            bracket -= 1
        if bracket == 0:
            break
        c += 1
    return c


if __name__ == "__main__":
    main()
