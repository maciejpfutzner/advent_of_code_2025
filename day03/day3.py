infile = open("input.txt")
#infile = open("ex.txt")

p1 = 0
p2 = 0

def max_joltage(digits, n):
    """Get largest number with n of digits"""
    if n == 1:
        return max(digits)
    
    first = max(digits[:-(n-1)]) # Largest of all but last n-1 digits
    first_pos = digits.index(first)
    return first * 10**(n-1) + max_joltage(digits[first_pos+1:], n-1)


for bank in infile:
    jolts = [int(c) for c in bank.strip()]
    p1 += max_joltage(jolts, 2)
    p2 += max_joltage(jolts, 12)

print(p1)
print(p2)
