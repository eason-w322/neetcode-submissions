class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [0]*(n+1)
        for i in range(n+1):
            x = i
            count = 0
            while x > 0:
                count += x % 2
                x = x // 2
            results[i] = count
        return results