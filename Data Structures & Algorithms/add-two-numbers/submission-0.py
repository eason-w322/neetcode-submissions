# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            value = l1.val + l2.val + carry
            carry = 0
            if value >= 10:
                value = value - 10
                carry = 1
            curr.next = ListNode(val = value)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            value = carry + l1.val
            carry = 0
            if value >= 10:
                value -= 10
                carry = 1
            curr.next = ListNode(val = value)
            curr = curr.next
            l1 = l1.next
        
        while l2:
            value = carry + l2.val
            carry = 0
            if value >= 10:
                value -= 10
                carry = 1
            curr.next = ListNode(val = value)
            curr = curr.next
            l2 = l2.next
        
        if carry == 1:
            curr.next = ListNode(1)
        
        return dummy.next

        
            
        