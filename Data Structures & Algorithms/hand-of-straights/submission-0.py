class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        seen = {}
        for card in hand:
            seen[card] = seen.get(card, 0) + 1
        

        for start in sorted(seen):
            needed = seen[start]
            if needed > 0:
                for k in range(start, start + groupSize):
                    if k not in seen or seen[k] < needed:
                        return False
                    seen[k] -= needed
        
        return True