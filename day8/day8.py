import math
from math import sqrt

def main(part1):
    lines = [tuple(map(int, line.split(','))) for line in open('input').read().split('\n')]
    edges = []
    for i in range(0,len(lines)):
        p1 = lines[i]
        for j in range(i+1,len(lines)):
            p2 = lines[j]
            edges.append((p1,p2,sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2) + math.pow(p1[2] - p2[2], 2))))
    edges.sort(key=lambda e:e[2])
    networks = []
    counter = 0
    for p1,p2,_ in edges:
        nwp1, nwp2 = set(),set()
        for network in networks:
            if p1 in network:
                nwp1 = network
            if p2 in network:
                nwp2 = network
        if nwp1:
            networks.remove(nwp1)
        if nwp2 and nwp2 is not nwp1:
            networks.remove(nwp2)
        merged = nwp1 | nwp2 | {p1, p2}
        networks.append(merged)

        if counter == 1000 and part1:
            networks.sort(key=len, reverse=True)
            return (len(networks[0]) * len(networks[1]) * len(networks[2]))
        if len(networks) == 1 and len(networks[0]) == len(lines) and not part1:
            return p1[0] * p2[0]

        counter+=1

print(main(True))
print(main(False))