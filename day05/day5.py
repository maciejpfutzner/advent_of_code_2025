ranges_, items_ = open("input.txt").read().split("\n\n")

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
