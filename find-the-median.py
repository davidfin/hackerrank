def partition(A, lo, hi):
    i=lo-1
    pivot = A[hi]
    for j in range(lo, hi):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[hi] = A[hi], A[i+1]
    return (i+1)
    
def quicksort(ar, l, r, idx):
    if (l < r):
        m = partition(ar, l, r)
        if (idx == m - l + 1):
            return ar[m]
        elif (idx <= m - l):
            return quicksort(ar, l, m - 1, idx)
        else:
            return quicksort(ar, m + 1, r, idx - (m - l + 1))
    else:
        return ar[l]

n = int(raw_input())
a = map(int, raw_input().strip().split(' '))

print quicksort(a, 0, n - 1, (n + 1) / 2)