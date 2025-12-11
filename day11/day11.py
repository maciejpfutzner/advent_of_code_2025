infile = open("input.txt")
#infile = open("ex.txt")

outputs = {}
for line in infile:
    elements = line.strip().split()
    node = elements[0].strip(":")
    assert node not in outputs
    outputs[node] = elements[1:]

#print(outputs)

mem = {}
def get_n_paths(node):
    if node in mem:
        return mem[node]
    if node == "out":
        return 1
    result = sum(get_n_paths(n) for n in outputs[node])
    mem[node] = result
    return result

print(get_n_paths("you"))

