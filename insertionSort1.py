#!/bin/python
def print_list(ar):
	print(' '.join(map(str, ar)))

def insertionSort(ar):
	# edge case
	if len(ar) == 1:
		print_list(ar)
		return(ar)
	else:
		e = ar[-1]
		n = len(ar) - 1

		for i in reversed(range(n)):
		if e < ar[i]:
			ar[i + 1] = ar[i]
			print_list(ar)

			if i == 0:
				ar[0] = e
				print_list(ar)
				break
		else:
			ar[i + 1] = e
			print_list(ar)
			break

	return(ar)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
