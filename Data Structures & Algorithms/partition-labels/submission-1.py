class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        n = len(s)
        for i in range(n):
            last[s[i]] = i
    
        results = []
        right_end = 0
        furthest = 0
        start = 0
        for j in range(n):
            furthest = max(furthest, last[s[j]])
            if furthest == j:
                results.append(furthest - start + 1)
                start = j + 1
        
        return results



        

