class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # dp is a dict: {running_total: number_of_ways to finish from here}
        # base row (i == n): 1 way if total == target, else 0
        dp = {target: 1}

        # fill rows from i = n-1 down to 0
        for i in range(n - 1, -1, -1):
            num = nums[i]
            nxt = {}
            for total, ways in dp.items():
                # reverse of "add = backtrack(i+1, total+num)":
                # a cell at (i, t) feeds sums t+num and t-num in the next row,
                # so cell (i, t) collects from totals t+num and t-num below it
                nxt[total - num] = nxt.get(total - num, 0) + ways
                nxt[total + num] = nxt.get(total + num, 0) + ways
            dp = nxt

        return dp.get(0, 0) 
        