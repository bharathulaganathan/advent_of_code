import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = "input" + ".txt"
file_path = os.path.join(base_dir, input_file)

LITERS = 150

containers = list()
with open(file_path, "r") as input:
    for row in input:
        row = row.strip().split(" ")
        for container in row:
            containers.append(int(container))

COMBINATIONS = 0

def main():
    containers.sort(reverse=True)
    make_combinations(LITERS, containers)
    print(COMBINATIONS)

def make_combinations(capacity, remaining):
    global COMBINATIONS
    while remaining:
        container =  remaining.pop()
        new_capacity = capacity - container
        if new_capacity == 0:
            COMBINATIONS += 1
        elif new_capacity > 0:
            new_remaining = remaining.copy()
            make_combinations(new_capacity, new_remaining)





if __name__ == "__main__":
    main()
