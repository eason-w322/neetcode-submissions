from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.same_vertical = defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x,y)] += 1
        self.same_vertical[x].append(y)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        count = 0
        for py in self.same_vertical[qx]:
            if py == qy:
                continue
            distance = qy - py
            for d in (qx - abs(distance), qx + abs(distance)):
                if qy in self.same_vertical[d] and py in self.same_vertical[d]:
                    count += self.points[(d, qy)]*self.points[(d, py)]
        return count
        
