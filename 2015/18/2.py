import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = "input" + ".txt"
file_path = os.path.join(base_dir, input_file)

STEPS = 100

lights = list()
with open(file_path, "r") as input:
    for row in input:
        row = row.strip()
        lights.append(list(row))


def main():
    global lights
    for i in [0, len(lights)-1]:
        for j in [0, len(lights[i])-1]:
            lights[i][j] = "#"
    for _ in range(STEPS):
        new_lights = [["." for _ in range(len(lights[0]))] for _ in range(len(lights))]
        for i in [0, len(new_lights)-1]:
            for j in [0, len(new_lights[i])-1]:
                new_lights[i][j] = "#"
        for i in range(len(lights)):
            for j in range(len(lights[i])):
                lights_on = 0 if lights[i][j] == "." else -1
                for k in range(max(0,i-1),min(len(lights),i+2)):
                    for l in range(max(0,j-1),min(len(lights[k]),j+2)):
                        if lights[k][l] == "#":
                            lights_on += 1
                if lights[i][j] == "#" and 2 <= lights_on <= 3:
                    new_lights[i][j] = "#"
                elif lights[i][j] == "." and lights_on == 3:
                    new_lights[i][j] = "#"
        lights = new_lights
    lights_on = 0
    for i in range(len(lights)):
        for j in range(len(lights[i])):
            if lights[i][j] == "#":
                lights_on += 1
    print(lights_on)


if __name__ == "__main__":
    main()