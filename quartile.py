N = int(raw_input())    
X = [float(x) for x in raw_input().split(" ")]

middle = N/2
if(len(X) % 2 != 0):
	middle = middle + 1

A = sorted(X)
lower = A[0:N/2]
upper = A[middle:]

def median(numbers):
	numbers = sorted(numbers)
	center = len(numbers) / 2
	if len(numbers) % 2 == 0:
		return int(sum(numbers[center - 1:center + 1]) / 2.0)
	else:
		return int(numbers[center])

print median(lower)
print median(A)
print median(upper)

