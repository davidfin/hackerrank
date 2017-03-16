def solution(a):

    # create a dictionary of (array value, index) pair 
    m = {}
    for i in range(len(a)):
        value = a[i]
        m[value] = i 
        
        
    sorted_a = sorted(a)
    ret = 0
    
    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            ret +=1
            ind_to_swap = m[ sorted_a[i] ]
            m[ a[i] ] = ind_to_swap
            a[i], a[ind_to_swap] = sorted_a[i], a[i]
    return ret

raw_input()
a = [int(i) for i in raw_input().split(' ')]

asc=solution(list(a))
desc=solution(list(reversed(a)))
print min(asc,desc)