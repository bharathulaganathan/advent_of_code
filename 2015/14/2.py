import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = "input" + ".txt"
file_path = os.path.join(base_dir, input_file)

deers = []
with open(file_path, "r") as input:
    for row in input:
        row = row.strip().split(" ")
        deer = row[0]
        fly = row[3]
        time = row[5]
        rest = row[-2]
        deers.append({"deer": deer, "fly": fly, "time": time, "rest": rest})


def main():
    print(deers)

if __name__ == "__main__":
    main()
