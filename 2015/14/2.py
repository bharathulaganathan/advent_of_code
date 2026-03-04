import os
import heapq

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = "input" + ".txt"
file_path = os.path.join(base_dir, input_file)

TIME = 2503

deers = []
with open(file_path, "r") as input:
    for row in input:
        row = row.strip().split(" ")
        deer = row[0]
        speed = int(row[3])
        fly = int(row[6])
        rest = int(row[-2])
        deers.append({"deer": deer, "speed": speed, "fly": fly, "rest": rest})


def main():
    now = 0
    standings = dict()
    for deer in deers:
        standings[deer["deer"]] = dict()
        standings[deer["deer"]]["points"] = 0
        standings[deer["deer"]]["distance"] = 0
    while now < TIME:
        round = dict()
        for deer in deers:
            state = now % (deer["fly"] + deer["rest"])
            if state < deer["fly"]:
                standings[deer["deer"]]["distance"] += deer["speed"]
            round.setdefault(standings[deer["deer"]]["distance"], []).append(deer["deer"])
        rank = []
        for key, val in round.items():
            rank.append((key,val))
        heapq.heapify_max(rank)
        best = heapq.heappop_max(rank)
        for deer in best[1]:
            standings[deer]["points"] += 1
        now += 1
    prize = []
    for val in standings.values():
        prize.append(val["points"])
    heapq.heapify_max(prize)
    print(heapq.heappop_max(prize))

if __name__ == "__main__":
    main()
