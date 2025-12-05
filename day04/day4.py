infile = open("input.txt")
#infile = open("ex.txt")

G = []
for line in infile:
    G.append([c for c in line.strip()])

R = len(G)
C = len(G[0])
p1 = 0

def find_accessible(G):
    accessible = set()
    for r in range(R):
        for c in range(C):
            n_neighbours = 0
            if G[r][c] != '@':
                continue
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < R and 0 <= cc < C:
                        if G[rr][cc] == '@' and not (dr == dc ==0):
                            n_neighbours +=1
            if n_neighbours < 4:
                accessible.add((r, c))
    return accessible

print('Part 1:', len(find_accessible(G)))


p2 = 0
while True:
    accessible = find_accessible(G)
    if len(accessible) == 0:
        break
    else:
        p2 += len(accessible)

    # Remove the rolls
    for r in range(R):
        for c in range(C):
            if (r, c) in accessible:
                G[r][c] = '.'
print('Part 2:', p2)
        
