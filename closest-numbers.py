n = int(raw_input())
arr = list(map(int, raw_input().split(" ")))

# should select a sorting algoritm here 
array = sorted(arr)
    
pairs = zip(array, array[1:])    
min_diff = min(b - a for a, b in pairs)

result = []
for a,b in pairs: 
    if (b-a == min_diff): 
        result += [a,b]

print ' '.join(map(str, result))