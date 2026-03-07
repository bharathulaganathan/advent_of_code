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
MINIMUM = len(containers)

def main():
    containers.sort(reverse=True)
    make_combinations(LITERS, list(), containers)
    print(COMBINATIONS)

def make_combinations(capacity, current, remaining):
    global COMBINATIONS, MINIMUM
    while remaining:
        container = remaining.pop()
        new_capacity = capacity - container
        len_current = len(current)
        if new_capacity == 0:
            if len_current == MINIMUM:
                COMBINATIONS += 1
            if len_current < MINIMUM:
                MINIMUM = len_current
                COMBINATIONS = 1
        elif new_capacity > 0 and len_current < MINIMUM:
            new_current = current.copy()
            new_current.append(container)
            new_remaining = remaining.copy()
            make_combinations(new_capacity, new_current, new_remaining)





if __name__ == "__main__":
    main()
