N = int(raw_input()) 
X = [int(x) for x in raw_input().split(" ")]
F = [int(x) for x in raw_input().split(" ")]

def unravel_input(X, F, N):
	S = []
	for i in range(0,N):
		temp = [X[i]]*F[i]
		S = S + temp
	return S 

def quartile(X): 
	N = len(X)
	middle = N/2
	if(len(X) % 2 != 0):
		middle = middle + 1
	A = sorted(X)
	lower = A[0:N/2]
	upper = A[middle:]
	return median(lower), median(A), median(upper)

def median(numbers):
	numbers = sorted(numbers)
	center = len(numbers) / 2
	if len(numbers) % 2 == 0:
		return int(sum(numbers[center - 1:center + 1]) / 2.0)
	else:
		return int(numbers[center])


S = unravel_input(X, F, N)
q1, q2, q3 = quartile(S)
print float(q3 - q1)
