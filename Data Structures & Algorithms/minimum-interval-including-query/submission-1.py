import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x : x[0])
        q_sorted = sorted((q, idx) for idx, q in enumerate(queries))
        min_heap = []
        i = 0
        n = len(intervals)
        results = [-1] * len(q_sorted)
        
        for q, idx in q_sorted:
            while i <= n - 1 and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            results[idx] = min_heap[0][0] if min_heap else -1
        
        return results

