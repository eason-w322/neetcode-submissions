# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and fast.next and not fast.next.next:
                break
        
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            if not next_node:
                break
            curr = next_node
        
        list1 = head
        while list1 and curr:
            next_list1 = list1.next
            list1.next = curr
            next_curr = curr.next
            curr.next = next_list1
            list1 = next_list1
            curr = next_curr

