class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        results = []

        start = intervals[0][0]
        end = intervals[0][1]

        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] > end:
                results.append([start, end])
                start = intervals[i][0]
            end = max(end, intervals[i][1])
        results.append([start, end])
        
        return results
                


