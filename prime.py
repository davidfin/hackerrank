from math import sqrt
def prime(a):
    if a < 2: 
        return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True    

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    
    print("Prime" if prime(n) else "Not prime")