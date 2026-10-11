# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        curr = head
        dummy = ListNode()
        temp = dummy
        while count - k >= 0:
            old_head = curr
            prev = None
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            temp.next = prev
            temp = old_head
            count -= k
        temp.next = curr
        
        return dummy.next
            


        