class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        keys = sorted(count, key = lambda x: count[x], reverse = True)
        return keys[:k]


