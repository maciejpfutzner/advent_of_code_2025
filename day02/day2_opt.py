input_ = open("input.txt").read().strip()
#input_ = open("ex.txt").read().strip()
p1 = 0
p2 = 0

def bounds(n):
    """Return largest number with n digits and smallest with n+1"""
    return int('9'*n), int('1'+'0'*n)


for range_ in input_.split(","):
    first, last = range_.split("-")
    # Get the range of digits
    d_first, d_last = len(first), len(last)
    if d_first == d_last:
        # Usually the range is within the same number of digits
        ranges_new = [(int(first), int(last))]
        ds = [d_first]
    else:
        # If the range crosses a boundary, split it
        all_bounds = (
                [int(first)]
                + [dd for d in range(len(first), len(last)) for dd in bounds(d)]
                + [int(last)]
                )
        ranges_new = [(all_bounds[i], all_bounds[i+1]) for i in range(0, len(all_bounds), 2)]
        ds = range(d_first, d_last + 1)
        #print(f"Splitting ({first}, {last}) into:")
        #for r, d in zip(ranges_new, ds):
        #    print(f"{r} with {d} digits")

    # Iterate over the new ranges
    for range_new, d in zip(ranges_new, ds):
        first, last = range_new

        # Find all divisors of the number of digits
        divisors = [i for i in range(d//2, 0, -1) if d % i == 0]
        #print(f"Range {range_new} with {d} digits. Divisors: {divisors}")

        for n in range(first, last + 1):
            num = str(n)
            for i in divisors:
                if num[:i] * (d//i) == num:
                    p2 += n
                    if i == d//2 and d % 2 == 0:
                        p1 += n
                    break

print(p1)
print(p2)
