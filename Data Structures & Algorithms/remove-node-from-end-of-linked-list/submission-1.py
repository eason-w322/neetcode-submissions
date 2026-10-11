# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        removed_position = length + 1 - n
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while removed_position:
            prev = curr
            curr = curr.next
            removed_position -= 1
        
        prev.next = curr.next
        return dummy.next
        

        

        