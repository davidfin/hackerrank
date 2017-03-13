#!/bin/python
def print_list(ar):
	print(' '.join(map(str, ar)))

def insertionSort(ar):
    if len(ar) == 1:
        print_list(ar)
        return(ar)
    else:
        for j in range(1, len(ar)):
            for i in reversed(range(j)):
                if ar[i + 1] < ar[i]:
                    ar[i], ar[i + 1] = ar[i + 1], ar[i]
                else:
                    break
            
            print_list(ar)
        
        return(ar)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
