class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        a_can = b_can = c_can = False
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                if a == x:
                    a_can = True
                
                if b == y:
                    b_can = True

                if c == z:
                    c_can = True
            
        return a_can and b_can and c_can
