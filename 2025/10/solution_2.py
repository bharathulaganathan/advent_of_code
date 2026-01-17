import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

machines = []

with open(file_path, "r") as input:
    for row in input:
        row = row.strip()
        elements = row.split(" ")
        lights = list(elements.pop(0).lstrip("[").rstrip("]"))
        joltages = elements.pop(-1).lstrip("{").rstrip("}").split(",")
        joltages = tuple(map(int, joltages))
        wirings = list()
        for element in elements:
            element = element.lstrip("(").rstrip(")").split(",")
            element = list(map(int, element))
            wirings.append(element)
        machines.append({"lights": lights, "wirings": wirings, "joltages": joltages})

def runs(joltages, wirings, press, status):
    new_status = set()
    for wiring in wirings:
        for state in status:
            new_state = list(state).copy()
            for wire in wiring:
                new_state[wire] += 1
            new_state = tuple(new_state)
            if new_state == joltages:
                return press
            new_status.add(new_state)
    return runs(joltages, wirings, press+1, new_status)

presses = 0
for machine in machines:
    presses += runs(machine["joltages"], machine["wirings"], 1, [[0 for _ in range(len(machine["joltages"]))]])
    print(presses)

print(presses)
