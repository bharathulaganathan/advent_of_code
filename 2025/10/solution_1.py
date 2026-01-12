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
        joltages = list(map(int, joltages))
        wirings = list()
        for element in elements:
            element = element.lstrip("(").rstrip(")").split(",")
            element = list(map(int, element))
            wirings.append(element)
        machines.append({"lights": lights, "wirings": wirings, "joltages": joltages})

def runs(lights, wirings, press, status):
    new_status = []
    for wiring in wirings:
        for state in status:
            new_state = state.copy()
            for wire in wiring:
                if new_state[wire] == ".":
                    new_state[wire] = "#"
                else:
                    new_state[wire] = "."
            if new_state == lights:
                return press
            new_status.append(new_state)
    return runs(lights, wirings, press+1, new_status)

presses = 0
for machine in machines:
    presses += runs(machine["lights"], machine["wirings"], 1, [["."]*len(machine["lights"])])

print(presses)
