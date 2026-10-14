class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        results = []
        for x, y in points:
            heapq.heappush(min_heap,(x**2 + y**2, x, y))
        for _ in range(k):
            dist, x, y = heapq.heappop(min_heap)
            results.append([x,y])
        return results

