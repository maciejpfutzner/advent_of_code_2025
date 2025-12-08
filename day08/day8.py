from collections import Counter

infile = open("input.txt")
max_connections_p1 = 1000

# For the example
#infile = open("ex.txt")
#max_connections_p1 = 10

boxes = []
for line in infile:
    boxes.append([int(x) for x in line.split(',')])

dists = []
for i, box1 in enumerate(boxes):
    for j, box2 in enumerate(boxes[:i]):
        d = sum((x2-x1)**2 for x1, x2 in zip(box1, box2))
        dists.append((d, i, j))
dists.sort()

# Dict of circuit_ID: list of boxes
circuits = {i: [i] for i in range(len(boxes))}
# Dict of box: circuit ID
circuit_ids = {i: i for i in range(len(boxes))}

n_conns = 0
for _, j, i in dists:
    if n_conns == max_connections_p1:
        sizes = Counter(circuit_ids.values())
        #print(sizes)
        x, y, z = (mc[1] for mc in sizes.most_common(3))
        print(f"There are {len(sizes)} circuits, top three have {x}, {y} and {z} boxes, respectively")
        print(f"Part 1: {x*y*z}")
    n_conns += 1

    cid_i = circuit_ids[i]
    cid_j = circuit_ids[j]
    if cid_i != cid_j:
        # Assign all boxes in circuit j to circuit i
        for box in circuits[cid_j]:
            circuit_ids[box] = cid_i
        # Merge the lists of boxes in the two circuits
        circuits[cid_i].extend(circuits.pop(cid_j))

    if len(circuits) == 1:
        # Only one big circuit left
        print("Part 2:", boxes[i][0] * boxes[j][0])
        break
