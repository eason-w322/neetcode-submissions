class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        seen = set()
        candidates = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            if num - 1 in seen:
                continue
            candidates.add(num)
        
        global_max = 0
        count = 1
        for candidate in candidates:
            while candidate + 1 in seen:
                count += 1
                candidate += 1
            global_max = max(count, global_max)
            count = 1
        
        return global_max
            

        
