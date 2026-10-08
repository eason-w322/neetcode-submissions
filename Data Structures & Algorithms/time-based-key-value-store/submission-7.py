class TimeMap:

    def __init__(self):
        self.timeMap = {}
        self.timeTrack = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = {}
        self.timeMap[key][timestamp] = value
        self.timeTrack[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap or timestamp < self.timeTrack[key][0]:
            return ""
        if timestamp in self.timeMap[key]:
            return self.timeMap[key][timestamp]
        
        time = self.timeTrack[key]
        left = 0
        right = len(time) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if time[mid] > timestamp:
                right = mid - 1
            else:
                left = mid
        time_offset = self.timeTrack[key][left]
        return self.timeMap[key][time_offset]
        