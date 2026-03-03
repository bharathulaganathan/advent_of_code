import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = "input" + ".txt"
file_path = os.path.join(base_dir, input_file)

happiness = dict()
people = set()
with open(file_path, "r") as input:
    for row in input:
        row = row.strip().split(" ")
        person = row[0]
        happy = int(row[3])
        if row[2] == "lose":
            happy = -happy
        next = row[-1][:-1]
        people.add(person)
        happiness[(person, next)] = happy


def main():
    best = create_party([], people.copy())
    print(best)

def create_party(current, remaining):
    best = float("-inf")
    if remaining:
        for person in remaining:
            new_current = current.copy()
            new_current.append(person)
            new_remaining = remaining.copy()
            new_remaining.remove(person)
            best = max(best, create_party(new_current, new_remaining))
    else:
        return get_happiness(current)
    return best

def get_happiness(arrangement):
    total_happy = 0
    for i in range(len(arrangement)):
        total_happy += happiness[(arrangement[i], arrangement[i-1])]
        total_happy += happiness[(arrangement[i], arrangement[(i+1)%len(arrangement)])]
    return total_happy


if __name__ == "__main__":
    main()
