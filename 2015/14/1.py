import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = "input" + ".txt"
file_path = os.path.join(base_dir, input_file)

TIME = 2503

deers = []
with open(file_path, "r") as input:
    for row in input:
        row = row.strip().split(" ")
        deer = row[0]
        speed = int(row[3])
        fly = int(row[6])
        rest = int(row[-2])
        deers.append({"deer": deer, "speed": speed, "fly": fly, "rest": rest})


def main():
    longest = 0
    for deer in deers:
        dist = (TIME // (deer["fly"] + deer["rest"])) * (deer["speed"]*deer["fly"])
        rem = TIME % (deer["fly"] + deer["rest"])
        dist += min(rem,deer["fly"]) * deer["speed"]
        longest = max(longest, dist)
    print(longest)

if __name__ == "__main__":
    main()
