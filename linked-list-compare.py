def CompareLists(headA, headB):
    
    while (headA != None and headB !=None):
        if (headA.data != headB.data): 
            return 0
        headA = headA.next
        headB = headB.next
        
    if (headA == None and headB == None): 
        return 1
    else: 
        return 0