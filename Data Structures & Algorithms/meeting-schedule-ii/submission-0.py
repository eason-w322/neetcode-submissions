"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(x.start for x in intervals)
        end = sorted(x.end for x in intervals)

        best = 0
        room_needed = 0
        j = 0
        i = 0
        while i <= len(start) - 1:
            if start[i] < end[j]:
                room_needed += 1
                best = max(room_needed, best)
                i += 1
            
            else:
                room_needed -= 1
                j += 1
        
        return best

