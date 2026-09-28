class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
        
        candidates = []
        for num in seen:
            ###if num - 1 in seen and num + 1 in seen:
                ###continue
            if num - 1 in seen:
                continue
            candidates.append(num)
        
        count = 1
        global_max = 0
        for c in candidates:
            while c + 1 in seen:
                c += 1
                count += 1
            global_max = max(count, global_max)
            count = 1
        return global_max
            
                
            
            

        
