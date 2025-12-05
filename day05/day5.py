ranges_, items_ = open("input.txt").read().split("\n\n")
#ranges_, items_ = open("ex.txt").read().split("\n\n")

ranges = []
for line in ranges_.split():
    low, high = line.strip().split("-")
    ranges.append((int(low), int(high)))

items = [int(item) for item in items_.split()]

p1 = 0
for item in items:
    for low, high in ranges:
        if low <= item <= high:
            p1 += 1
            break
print(p1)

p2 = 0
while len(ranges) > 0:
    low, high = ranges[0]
    overlaps = False

    # Check if the new range overlaps with any of the other ones
    for i in range(1, len(ranges)):
        ll, hh = ranges[i]
        # No overlap if high < ll or low > hh, so overlap if high >= ll and low <= hh
        if high >= ll and low <= hh:
            # If they overlap, merge the ranges
            ranges[i] = min(ll, low), max(hh, high)
            overlaps = True
            break

    if not overlaps:
        # If no overlap, just count the size
        p2 += high - low + 1

    # In any case, remove the range we just processed
    ranges = ranges[1:]
print(p2)
            

