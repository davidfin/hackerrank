def is_matched(expression):
    stack = []
    dicty = {'(':')', '[':']', '{':'}'}
    
    for x in expression:
        if dicty.get(x):
            stack.append(dicty[x])
        else:
            if len(stack) == 0 or x != stack[len(stack)-1]:
                return False
            stack.pop()
    return len(stack) == 0

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"