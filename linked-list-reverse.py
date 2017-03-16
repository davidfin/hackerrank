def Reverse(head):
    
    if (head == None or head.next == None):
        return head
    
    newHead = Reverse(head.next) # reverse all but the first
    head.next.next = head # original second point to the first
    head.next = None # original first point to None

    return newHead