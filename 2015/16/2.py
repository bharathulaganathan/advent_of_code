import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = "input" + ".txt"
file_path = os.path.join(base_dir, input_file)

sue = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""

aunts = dict()
with open(file_path, "r") as input:
    for row in input:
        row = row.strip().split(" ")
        aunt = int(row[1][:-1])
        aunts[aunt] = dict()
        for i in range(2, len(row), 2):
            aunts[aunt][row[i][:-1]] = int(row[i+1].strip(","))

target = dict()
sue = sue.strip().split("\n")
for i in range(0, len(sue)):
    c = sue[i].split(": ")
    target[c[0]] = int(c[1])
sue = target

def main():
    for aunt, things in aunts.items():
        could_be = True
        for thing in things:
            if thing in ["cats", "trees"]:
                if not things[thing] > sue[thing]:
                    could_be = False
                    break
            elif thing in ["pomeranians", "goldfish"]:
                if not things[thing] < sue[thing]:
                    could_be = False
                    break
            else:
                if not things[thing] == sue[thing]:
                    could_be = False
                    break
        if could_be:
            print(aunt)
        


if __name__ == "__main__":
    main()
