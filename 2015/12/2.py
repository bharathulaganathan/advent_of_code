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
        nums = []
        c = 0
        while c < len(doc):
            if is_num(doc[c]):
                num = 0
                c, num = get_num(c, doc)
                nums.append(int(num))
            elif is_red(c, doc):
                c = get_dict(c, doc)
            c += 1
        total = 0
        for num in nums:
            total += num
        print(total)


def is_num(char):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if char in nums:
        return True
    return False


def get_num(index, num):
    new_num = ""
    while index < len(num):
        if is_num(num[index]):
            if num[index - 1] == "-":
                new_num = "-"
            new_num = new_num + num[index]
            index += 1
        else:
            break
    return index, new_num


def is_red(index, json):
    if not json[index : index + 5] == '"red"':
        return False
    json_len = len(json)
    while index >= 0 and index < json_len:
        if json[index] == "[":
            if json[index - 1] == ":":
                return True
            else:
                return False
        elif json[index] == ":":
            return True
        index -= 1
    return False


def get_dict(index, json):
    count = 1
    index += 4
    json_len = len(json)
    while count > 0 and index < json_len - 1:
        index += 1
        if json[index] == "}":
            count -= 1
        elif json[index] == "{":
            count += 1
    return index


if __name__ == "__main__":
    main()
