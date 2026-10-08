class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            k = (left + right) // 2
            if sum((p + k - 1)//k for p in piles) <= h:
                right = k 
            else:
                left = k + 1
        return left
  