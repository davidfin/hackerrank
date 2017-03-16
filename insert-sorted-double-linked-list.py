def SortedInsert(head, data):
    newNode = Node(data = data)
        
    # insert empty 
    if (head == None): 
        return newNode;
    # insert in front of list
    elif (data < head.data): 
        newNode.next = head
        head.prev = newNode
        return newNode
    else: 
        # Walk list with 2 pointers
        n1 = None
        n2 = head
        
        while (n2 != None and n2.data < data):
            n1 = n2
            n2 = n2.next
        
        # insert at end of list
        if (n2 == None):
            n1.next = newNode
            newNode.prev = n1
        # insert in empty list
        else:
            n1.next = newNode
            n2.prev = newNode
            newNode.prev = n1
            newNode.next = n2
        
        return head
