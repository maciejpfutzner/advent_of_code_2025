pos = 50
p1 = 0
p2 = 0

infile = open("input.txt")
#infile = open("ex.txt")

for line in infile:
    dir_, n = line[0], int(line.strip()[1:])
    if dir_ == 'R':
        pos += n
        p2 += abs(pos // 100) # Add number of full rotations forward
    elif dir_ == 'L':
        # Similar to above but if ending on 0, we should count it
        # And starting from zero we should not count the initial part
        if pos == 0:
            p2 -= 1
        pos -= n
        p2 += abs((pos - 1) // 100)
    pos = pos % 100
    if pos == 0:
        p1 += 1

print(p1)
print(p2)


