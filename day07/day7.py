from collections import defaultdict

infile = open("input.txt")
#infile = open("ex.txt")

G = []
for line in infile:
    G.append(line.strip())
R = len(G)
C = len(G[0])

p1 = 0
beams = defaultdict(int)

for c in range(C):
    if G[0][c] == "S":
        beams[c] = 1
        break

for r in range(1, R):
    for c in range(C):
        if G[r][c] == "^" and c in beams:
            # Split the beam
            n_timelines = beams.pop(c)
            # There's always space on the sides, so no need to check for range
            beams[c-1] += n_timelines
            beams[c+1] += n_timelines
            p1 += 1

print("Part 1:", p1)
print("Part 2:", sum(beams.values()))
