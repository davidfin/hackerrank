n = int(raw_input()) 
arr = list(map(int, raw_input().strip().split(" ")))
k = 100 

def count_sort(n, arr):
    counts = [0]*k
    
    for i in range(n): 
        value = arr[i]
        counts[value] = counts[value] + 1

    return counts
    
print(' '.join(map(str, count_sort(n, arr))))