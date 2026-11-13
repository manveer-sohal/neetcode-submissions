"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        if not head:
            return None

       
        nodes = {None:None}
        #first pass, copy only next node
       
        curr = head
        prev = None
        copy = Node(x=-1)

        ret = Node(x=-1, next = copy)

        while curr:
            #copy nodes value
            copy.val = curr.val

            #Next node
            copy.next = Node(x = -1)
            
            #random node
            copy.random = None
            
            #add to hash
            nodes[curr] = copy

            if prev:
                prev.next = copy
            prev = copy
            curr=curr.next
            copy = Node(x=-1)
        
        prev.next = None

        #Second pass, copy the random 


        copy = ret.next
        curr = head
        prev = None

        while curr:
            
            
            random_node = nodes[curr.random]
            copy.random = random_node
            curr = curr.next
            copy = copy.next




        return ret.next