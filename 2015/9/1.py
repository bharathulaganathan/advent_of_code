import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

routes = {}
locations = set()
shortest = 0

with open(file_path, "r") as input:
    for row in input:
        row = row.strip()
        dep, arr_time = row.split(" to ")
        arr , time = arr_time.split(" = ")
        routes[(dep, arr)] = int(time)
        routes[(arr, dep)] = int(time)
        shortest += int(time)
        locations.add(dep)
        locations.add(arr)

def route_create(assigned, remaining):
    if len(remaining) == 0:
        global shortest
        distance = 0
        for i in range(len(assigned)-1):
            distance += routes[(assigned[i], assigned[i+1])]
        shortest = min(shortest, distance)
    else:
        for j in range(len(remaining)):
            new_assigned = assigned.copy()
            new_assigned.append(remaining[j])
            new_remaining = remaining.copy()
            new_remaining.pop(j)
            route_create(new_assigned, new_remaining)

route_create([], list(locations))

print(shortest)