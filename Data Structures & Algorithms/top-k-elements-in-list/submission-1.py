class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        min_heap = []
        for key, value in count.items():
            heapq.heappush(min_heap, (-value, key))
        
        results = []
        for _ in range(k):
            value, key = heapq.heappop(min_heap)
            results.append(key)
        return results


