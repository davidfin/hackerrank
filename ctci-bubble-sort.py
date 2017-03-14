n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

def swap(a, j): 
    temp = a[j] 
    a[j] = a[j+1] 
    a[j+1] = temp
    return a

global_num_swaps = 0

for i in range(n): 
    local_num_swaps = 0
    for j in range(n-1): 
        if a[j] > a[j+1]: 
            a = swap(a, j)
            global_num_swaps = global_num_swaps + 1
            local_num_swaps = local_num_swaps + 1
    
    if local_num_swaps ==0: 
        break

print "Array is sorted in " + str(global_num_swaps) + " swaps."
print "First Element: " + str(a[0])
print "Last Element: " + str(a[-1])