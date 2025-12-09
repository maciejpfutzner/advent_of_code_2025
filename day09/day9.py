infile = open("input.txt")
#infile = open("ex.txt")

coords = []
for line in infile:
    coords.append(tuple(int(n) for n in line.strip().split(',')))

p1 = 0
for i, (x1, y1) in enumerate(coords[1:]):
    for x2, y2 in coords[:i]:
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > p1:
            p1 = area
print(p1)
