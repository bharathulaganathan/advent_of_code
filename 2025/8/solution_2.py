import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)


boxes = []
with open(file_path, "r") as input:
    for row in input:
        x, y, z = row.strip().split(",")
        boxes.append((int(x), int(y), int(z)))

distances = []


for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distance = (
            (boxes[i][0] - boxes[j][0]) ** 2
            + (boxes[i][1] - boxes[j][1]) ** 2
            + (boxes[i][2] - boxes[j][2]) ** 2
        ) ** 0.5
        new_pair = {"r": distance, "pair": (boxes[i], boxes[j])}
        distances.append(new_pair)


circuit = set()
while True:
    last_connection = dict()
    min = distances[0]["r"]
    min_index = 0
    count = 0
    while count < len(distances):
        if (distances[count]["pair"][0] in circuit) and (
            distances[count]["pair"][1] in circuit
        ):
            del distances[count]
            count -= 1
        elif distances[count]["r"] < min:
            min = distances[count]["r"]
            min_index = count
        count += 1
    circuit.update(distances[min_index]["pair"])
    last_connection = distances[min_index]
    del distances[min_index]
    if len(circuit) >= len(boxes):
        break


print(last_connection["pair"][0][0] * last_connection["pair"][1][0])
