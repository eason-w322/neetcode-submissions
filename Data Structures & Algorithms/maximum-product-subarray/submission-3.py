class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, n):
            elem = nums[i]
            product_1 = dp_max[i-1] * elem
            product_2 = dp_min[i-1] * elem

            dp_max[i] = max(elem, product_1, product_2)
            dp_min[i] = min(elem, product_1, product_2)
        
        return max(dp_max)


