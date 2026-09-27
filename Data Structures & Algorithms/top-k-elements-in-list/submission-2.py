class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for key, value in count.items():
            bucket[value].append(key)
        
        results = []
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                results.append(num)
                if len(results) == k:
                    return results




