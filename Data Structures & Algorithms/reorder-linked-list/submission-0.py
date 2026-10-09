# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        mid = (count + 1 )// 2 
        count = 0
        curr = head
        while curr:
            count += 1
            if count == mid:
                list2 = curr.next
                curr.next = None
                break
            curr = curr.next
        
        prev = None
        while list2:
            next_node = list2.next
            list2.next = prev
            prev = list2
            if not next_node:
                break
            list2 = next_node

        curr = head
        while curr and list2:
            next_curr = curr.next
            curr.next = list2
            next_list2 = list2.next
            list2.next = next_curr
            list2 = next_list2
            curr = next_curr


