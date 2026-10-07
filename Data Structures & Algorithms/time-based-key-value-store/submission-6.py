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

        left = 0
        right = len(self.timeTrack[key]) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.timeTrack[key][mid] > timestamp:
                right = mid - 1
            elif self.timeTrack[key][mid] < timestamp:
                left = mid
        index = self.timeTrack[key][left]
        return self.timeMap[key][index]
        