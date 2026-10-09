class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            A, B = B, A
        m = len(A)
        n = len(B)
        half = (m + n + 1) // 2
        left = 0
        right = m
        while left <= right:
            i = (left + right) // 2
            j = half - i
            A_left = A[i-1] if i > 0 else -float("inf")
            A_right = A[i] if i < m else float("inf")
            B_left = B[j-1] if j > 0 else -float("inf")
            B_right = B[j] if j < n else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if (m + n) % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                return max(A_left, B_left)
            
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1

