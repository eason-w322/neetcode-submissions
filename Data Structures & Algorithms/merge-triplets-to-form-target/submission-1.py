class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        usable = []
        x, y, z = target
        for triplet in triplets:
            if triplet[0] <= x and triplet[1] <= y and triplet[2] <= z:
                usable.append(triplet)
        
        if not usable:
            return False
            
        a = max([i[0] for i in usable])
        b = max([i[1] for i in usable])
        c = max([i[2] for i in usable])

        if a == x and b == y and c == z:
            return True
        return False
