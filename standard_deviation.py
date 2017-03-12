import math
N = int(raw_input())
X = [float(x) for x in raw_input().split(" ")]

def mean(X, N): 
	sum = 0.0 
	for x in X: 
	sum = sum + x
	return sum/N 

def std(X, u, N): 
	top = 0
	for x in X: 
		top = top + (x - u)**2 

	return math.sqrt(top/N) 

if len(X) > 0: 
	u = mean(X, N)
	print std(X, u, N)
else: 
	print 0.0
