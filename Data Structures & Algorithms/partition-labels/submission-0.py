class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        
        results = []
        end = 0
        start = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                results.append(i - start + 1)
                start = end + 1
        return results


        

