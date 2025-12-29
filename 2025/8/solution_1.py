import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

COUNT = 1000

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

circuits = []
while COUNT > 0:
    min = distances[0]["r"]
    min_index = 0
    for i in range(len(distances)):
        if distances[i]["r"] < min:
            min = distances[i]["r"]
            min_index = i
    added = False
    found = False
    found_circuit = int()
    for j in range(len(circuits)):
        if (
            distances[min_index]["pair"][0] in circuits[j]
            and distances[min_index]["pair"][1] in circuits[j]
        ):
            found = True
            COUNT -= 1
            break
        elif (
            distances[min_index]["pair"][0] in circuits[j]
            or distances[min_index]["pair"][1] in circuits[j]
        ):
            if not (found):
                found = True
                found_circuit = j
                if distances[min_index]["pair"][0] in circuits[j]:
                    circuits[j].add(distances[min_index]["pair"][1])
                else:
                    circuits[j].add(distances[min_index]["pair"][0])
                added = True
                COUNT -= 1
            else:
                circuits[found_circuit].update(circuits[j])
                del circuits[j]
                break
    if not (added) and not (found):
        circuits.append(
            {distances[min_index]["pair"][0], distances[min_index]["pair"][1]}
        )
        COUNT -= 1
    del distances[min_index]
    print(COUNT)

connections = []

for i in range(len(circuits)):
    if len(connections) == 0:
        connections.append(len(circuits[i]))
    else:
        added = False
        for j in range(len(connections)):
            if len(circuits[i]) > connections[j]:
                connections.insert(j, len(circuits[i]))
                added = True
                break
        if not (added):
            connections.append(len(circuits[i]))

wire = connections[0] * connections[1] * connections[2]

print(wire)
