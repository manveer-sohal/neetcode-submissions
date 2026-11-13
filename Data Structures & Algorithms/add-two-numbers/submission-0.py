# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        


        

        curr1 = l1
        curr2 = l2
        curr =  ListNode()
        prev = None
        l3 = ListNode(next = curr)
        carry = 0

        while curr1 and curr2:

            total = curr1.val + curr2.val

            if total + carry >= 10:
                curr.val = total - 10 + carry
                carry = 1
            else:
                 curr.val = total + carry
                 carry = 0
            
            curr.next = ListNode()
            prev = curr
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next
        

        while curr1:

            total = curr1.val

            if total + carry >= 10:
                curr.val = total - 10 + carry
                carry = 1
            else:
                 curr.val = total + carry
                 carry = 0
            
            curr.next = ListNode()
            prev = curr
            curr = curr.next
            curr1 = curr1.next

        while curr2:

            total = curr2.val

            if total + carry >= 10:
                curr.val = total - 10 + carry
                carry = 1
            else:
                 curr.val = total + carry
                 carry = 0
            
            curr.next = ListNode()
            prev = curr
            curr = curr.next
            curr2 = curr2.next
           
        if carry: 
            curr.val = carry
        else:
            prev.next = None
        
        
        
        
        return l3.next


            
                

           






