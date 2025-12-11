infile = open("input.txt")
#infile = open("ex2.txt")

outputs = {}
for line in infile:
    elements = line.strip().split()
    node = elements[0].strip(":")
    assert node not in outputs
    outputs[node] = elements[1:]

# Part 1
mem = {}
def get_n_paths(node):
    if node in mem:
        return mem[node]
    if node == "out":
        return 1
    result = sum(get_n_paths(n) for n in outputs[node])
    mem[node] = result
    return result

print("Part 1:", get_n_paths("you"))

# Part 2
mem = {}
def get_n_paths(node, visited_dac=False, visited_fft=False):
    if (node, visited_dac, visited_fft) in mem:
        return mem[(node, visited_dac, visited_fft)]
    if node == "out":
        if visited_dac and visited_fft:
            return 1
        else:
            return 0
    if node == "dac":
        visited_dac = True
    if node == "fft":
        visited_fft = True
    result = sum(get_n_paths(n, visited_dac, visited_fft) for n in outputs[node])
    mem[(node, visited_dac, visited_fft)] = result
    return result

print("Part 2:", get_n_paths("svr"))
