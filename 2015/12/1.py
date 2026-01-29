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
                num_str = doc[c]
                c += 1
                while True:
                    if is_num(doc[c]):
                        num_str = num_str + doc[c]
                        c += 1
                    else:
                        nums.append(int(num_str))
                        break
            c += 1
        total = 0
        for num in nums:
            total += num
        print(total)


def is_num(char):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
    if char in nums:
        return True
    return False


if __name__ == "__main__":
    main()
