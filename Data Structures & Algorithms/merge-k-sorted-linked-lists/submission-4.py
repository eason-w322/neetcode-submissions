# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        priority_q = []
        for index, head in enumerate(lists):
            if head:
                heapq.heappush(priority_q, (head.val, index, head))

        dummy = ListNode
        dummy.next = None
        curr = dummy
        while priority_q:
            value, index, head = heapq.heappop(priority_q)
            curr.next = head
            curr = curr.next
            head = head.next
            if not head:
                continue
            heapq.heappush(priority_q, (head.val, index, head))
            
            
        return dummy.next

