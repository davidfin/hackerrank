"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    
    # create tail node
    tail = Node(data = data, next_node = None)
  
    if(head == None): 
        head = tail
        return head

    current = head
    
    while(current.next != None):
        current = current.next;
        
    current.next = tail
    return head