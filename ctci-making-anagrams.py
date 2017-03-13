from collections import Counter
def number_needed(a, b):
    ct_a = Counter(a) # dictionary for counting hashable objects!
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())    

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)