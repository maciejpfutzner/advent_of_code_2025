from functools import reduce

infile = open("input.txt")
#infile = open("ex.txt")
lines = infile.readlines()

G = []
for line in lines:
    G.append(line.split())

G = list(zip(*G))

p1 = 0
for problem in G:
    numbers = [int(n) for n in problem[:-1]]
    if problem[-1] == '+':
        p1 += sum(numbers)
    elif problem[-1] == '*':
        p1 += reduce(lambda x,y: x*y, numbers)
    else:
        raise ValueError(f"Unknown operator {problem[-1]}")

print(p1)

G = []
for line in lines:
    G.append(line.strip("\n"))

G, operators = G[:-1], G[-1].split()
R = len(G)
C = len(G[0])

p2 = 0
offset = 0

for op in operators:
    numbers = []

    for c in range(offset, C):
        number = ""
        for r in range(R):
            number += G[r][c]
        number = number.strip()

        if number == "":
            # This is the end of this problem
            break
        else:
            numbers.append(int(number))

    offset = c + 1
    assert len(numbers) > 0
    #print(op, numbers)
    if op == '+':
        p2 += sum(numbers)
    elif op == '*':
        p2 += reduce(lambda x,y: x*y, numbers)

print(p2)   
