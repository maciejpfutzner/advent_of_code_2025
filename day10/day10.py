from itertools import combinations
from collections import Counter

infile = open("input.txt")
#infile = open("ex.txt")

configs = []
for line in infile:
    elements = line.strip().split()
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    lights = elements[0][1:-1]
    lights = [i for i in range(len(lights)) if lights[i] == "#"]
    buttons = [eval(el) for el in elements[1:-1]]
    # Eval will parse (3) as 3 rather than (3,) -> turn ints into tuples
    buttons = [(b,) if isinstance(b, int) else b for b in buttons]
    joltages = [int(x) for x in elements[-1][1:-1].split(",")]
    configs.append((lights, buttons, joltages))

p1 = 0
for lights, all_buttons, joltages in configs:
    found = False
    for n_buttons in range(1, len(all_buttons)+1):
        if found:
            break

        for buttons in combinations(all_buttons, n_buttons):
            # Calculate number of presses for each button to get the correct output
            # We have m lights: y_0, ..., y_m-1
            # We also have n buttons, each with coefficients a_0, ..., a_m-1
            # These coefficients are either 0 or 1 (we only store the indices of the 1s)
            # Let's call coefficient a_i for button j: a_i^j
            # We press each button x times: x^j for button j, x^j = 0, 1, ...
            # For each light i: a_i^0 * x^j % 2 = y_i
            # The goals is to solve for the vector x with the smallest L1 norm |x| = x^0 + ... + x^n-1
            # Actually, we only care about the min value of |x|, not the actual solution
            # ...
            # Wait a moment! If each press is a toggle (we only care about x^j % 2),
            #   then it only makes sense to press a button once or not at all!
            # So the question is which buttons should be pressed, not how many times
            toggles = Counter([light for button in buttons for light in button])
            output = sorted([light for light in toggles if toggles[light] % 2])
            #print(f"Testing buttons {buttons} -> {output}")
            if output == lights:
                #print(f"Found solution - need to press {n_buttons} buttons: {buttons}")
                p1 += n_buttons
                found = True
                break
print(p1)
