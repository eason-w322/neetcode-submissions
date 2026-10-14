class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.score = nums
        heapq.heapify(self.score)
        while len(self.score) > k:
            heapq.heappop(self.score)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.score, val)
        while len(self.score) > self.k:
            heapq.heappop(self.score)
        return self.score[0]
        
        
