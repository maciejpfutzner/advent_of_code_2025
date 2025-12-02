input_ = open("input.txt").read().strip()
#input_ = open("ex.txt").read().strip()
p1 = 0
p2 = 0

for range_ in input_.split(","):
    first, last = range_.split("-")
    #print(first, last, len(first), len(last))
    for n in range(int(first), int(last) + 1):
        # TODO: Make this more efficient?
        num = str(n)
        l = len(num)

        # Part 1
        if l % 2 == 0 and num[:l//2] == num[l//2:]:
            p1 += n

        # Part 2
        # Check all dividers of l - possible group sizes
        for i in range(1, l//2+1):
            if l % i == 0:
                if num[:i] * (l//i) == num:
                    p2 += n
                    break

print(p1)
print(p2)
