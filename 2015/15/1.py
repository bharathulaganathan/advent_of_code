import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = "input" + ".txt"
file_path = os.path.join(base_dir, input_file)

TOTAL_TEASPOONS = 100

ingredients = dict()
with open(file_path, "r") as input:
    for row in input:
        row = row.strip().split(" ")
        ingredient = dict()
        name = row[0][:-1]
        ingredients[name] = dict()
        ingredients[name]["capacity"] = int(row[2][:-1])
        ingredients[name]["durability"] = int(row[4][:-1])
        ingredients[name]["flavor"] = int(row[6][:-1])
        ingredients[name]["texture"] = int(row[8][:-1])
        ingredients[name]["calories"] = int(row[10])
total_ingredients = len(ingredients.keys())


def main():
    print(get_permutation(0,[]))

def get_permutation(done, current):
    score = 0
    if done < total_ingredients-1:
        for i in range(0, max(1,TOTAL_TEASPOONS-sum(current))):
            new_current = current.copy()
            new_current.append(i)
            score = max(score, get_permutation(done+1,new_current))
    else:
        new_current = current.copy()
        new_current.append(TOTAL_TEASPOONS-sum(current))
        score = max(score, make_mixture(new_current))
    return score


def make_mixture(current):
    score = 1
    for property in ["capacity", "durability", "flavor", "texture"]:
        property_total = 0
        for i in range(len(current)):
            property_total += current[i] * ingredients[list(ingredients.keys())[i]][property]
        score *= max(property_total, 0)
    return score

if __name__ == "__main__":
    main()
