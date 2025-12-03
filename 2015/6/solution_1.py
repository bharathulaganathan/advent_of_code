import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

instructions = []

with open(file_path, "r") as input:
    for row in input:
        if row[:4] == "turn":
            row = row[5:]
        row = row.strip().split()
        row = {
            "mode": row[0],
            "start": list(map(int, row[1].split(","))),
            "end": list(map(int, row[3].split(",")))
            }
        instructions.append(row)

max_lights = 1000
lights = [[0]*max_lights for _ in range(max_lights)]

for switch in instructions:
    for x in range(switch["start"][0], switch["end"][0]+1):
        for y in range(switch["start"][1], switch["end"][1]+1):
            if switch["mode"] == "toggle":
                if lights[x][y] == 0:
                    lights[x][y] = 1
                elif lights[x][y] == 1:
                    lights[x][y] = 0
                else:
                    print("ERROR_1!")
            elif switch["mode"] == "on":
                lights[x][y] = 1
            elif switch["mode"] == "off":
                lights[x][y] = 0
            else:
                print("ERROR_2!")

lit = 0
for x in range(max_lights):
    for y in range(max_lights):
        if lights[x][y] == 1:
            lit += 1

print(lit)