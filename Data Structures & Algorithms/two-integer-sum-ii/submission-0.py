class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            complement = target - numbers[left]
            if complement == numbers[right]:
                return [left + 1, right + 1]
            
            elif complement < numbers[right]:
                right -= 1
            
            elif complement > numbers[right]:
                left += 1
            


        