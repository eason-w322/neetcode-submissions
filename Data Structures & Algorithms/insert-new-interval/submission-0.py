class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        results = []

        n = len(intervals)
        for i in range(n):
            if intervals[i][0] > end:
                results.append([start, end])
                start = intervals[i][0]
            end = max(end, intervals[i][1])
        
        results.append([start, end])
        return results