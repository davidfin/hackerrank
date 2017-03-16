def getPartitionIdx(A, lo, hi):
    i=lo-1
    pivot = A[hi]
    for j in range(lo, hi):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[hi] = A[hi], A[i+1]
    print(' '.join(map(str, A)))
    return (i+1)

def inplaceQuickSort(A, lo, hi):
    if(lo < hi):
        p=getPartitionIdx(A, lo, hi)
        inplaceQuickSort(A, lo, p-1)
        inplaceQuickSort(A, p+1, hi)


n = int(raw_input())
u = map(int, raw_input().strip().split(' '))

inplaceQuickSort(u, 0, n-1)