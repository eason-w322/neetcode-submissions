class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        n = len(intervals)
        i = 0
        results = []
        while i <= n - 1 and intervals[i][1] < start:
            results.append([intervals[i][0], intervals[i][1]])
            i += 1
        
        while i <= n - 1 and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        
        results.append([start, end])

        while i <= n - 1:
            results.append([intervals[i][0], intervals[i][1]])
            i += 1
        
        return results