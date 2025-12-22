infile = open("input.txt")
infile = open("ex.txt")

presents = []
spaces = []

blocks = infile.read().split("\n\n")
for block in blocks[:-1]:
    present = set()
    G = block.split("\n")[1:]
    for r in range(len(G)):
        for c in range(len(G[r])):
            if G[r][c] == "#":
                present.add((r,c))
    presents.append(present)

for line in blocks[-1].strip().split("\n"):
    elements = line.split()
    size = [int(x) for x in elements[0][:-1].split("x")]
    counts = [int(x) for x in elements[1:]]
    spaces.append((size, counts))


def move_present(present, x_offset, y_offset, rot=0):
    """Translate and rotate a present

    Rotation happens in 90* angles, along the midpoint (1,1)

    Args:
        present: set of (x,y) coords
        x_offset, y_offset: grid position integers
        rot: rotation index {0, 1, 2, 3}

    Returns:
    Updated present coords
    """
    present = {(x + x_offset, y + y_offset) for (x,y) in present}
    # TODO: Rotate it too!
    return present


def next_present(counts):
    new_counts = list(counts)
    for i, c in enumerate(counts):
        if c > 0:
            new_counts[i] = c-1
            return presents[i], tuple(new_counts)
    return set(), tuple()

mem = {}
def pack_present(space, remaining_presents):
    mem_key = (tuple(sorted(space)), tuple(remaining_presents))
    if mem_key in mem:
        return mem[mem_key]

    if sum(remaining_presents) == 0:
        return True

    present, remaining_presents = next_present(remaining_presents)
    results = []
    for x, y in space:
        # Can we fit the first present at any of the corners
        # FIXME: This isn't quite correct - the idea is that at least one part
        # of the present has to fit in an empty space, so we can go through all
        # empty spaces and try to fit the corner of the present. BUT, in the
        # current setup, the (0,0) coord is not necessarily part of the
        # present! We could rescale each present, so that (0,0) is in it
        # (and maybe make the rotations easier too)
        present_fits = False
        for rot in range(4):
            moved_present = move_present(present, x, y, rot)
            overlap = moved_present & space
            if len(overlap) == len(present):
                present_fits = True
                # The present fits in the space, let's solve the subproblem
                # (we have to do that for any configuration in which it fits)
                results.append(pack_present(space - overlap, remaining_presents))
        if not present_fits:
            results.append(False)

    result = any(results)
    mem[mem_key] = result
    return result


p1 = 0
for size, counts in spaces:
    space = {(x,y) for x in range(size[0]) for y in range(size[1])}
    if pack_present(space, tuple(counts)):
        p1 += 1
print(p1)
