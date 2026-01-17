import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

old_pwd = []
with open(file_path, "r") as input:
    for row in input:
        row = row.strip()
        old_pwd.append(row)


def main():
    new_pwd = []
    for pwd in old_pwd:
        counter = 0
        while True:
            pwd = increment(pwd)
            if check_straight(pwd) and check_letter(pwd) and check_pair(pwd):
                counter += 1
            if counter >= 2:
                new_pwd.append(pwd)
                break
    for pwd in new_pwd:
        print(pwd)


def increment(pwd):
    counter = len(pwd) - 1
    while counter >= 0:
        if pwd[counter] == "z":
            z_counter = counter
            while True:
                pwd = pwd[:z_counter] + "a" + pwd[z_counter + 1 :]
                z_counter -= 1
                if pwd[z_counter] != "z":
                    counter = z_counter
                    break
        pwd = pwd[:counter] + chr(ord(pwd[counter]) + 1) + pwd[counter + 1 :]
        return pwd


def check_straight(pwd):
    for c in range(len(pwd) - 2):
        if pwd[c + 1] == chr(ord(pwd[c]) + 1) and pwd[c + 2] == chr(ord(pwd[c]) + 2):
            return True
    return False


def check_letter(pwd):
    for c in range(len(pwd)):
        if pwd[c] == "i" or pwd[c] == "o" or pwd[c] == "l":
            return False
    return True


def check_pair(pwd):
    pair_counter = 0
    counter = 0
    while counter < len(pwd) - 1:
        if pwd[counter] == pwd[counter + 1]:
            pair_counter += 1
            counter += 2
        else:
            counter += 1
    if pair_counter >= 2:
        return True
    return False


if __name__ == "__main__":
    main()
