from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = {}
        self.same_vertical = {}
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x,y)] = self.points.get((x, y), 0) + 1
        if x not in self.same_vertical:
            self.same_vertical[x] = []
        self.same_vertical[x].append(y)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        count = 0
        if qx in self.same_vertical:
            for py in self.same_vertical[qx]:
                if py == qy:
                    continue
                distance = qy - py
                for d in (qx - abs(distance), qx + abs(distance)):
                    if d in self.same_vertical:
                        if qy in self.same_vertical[d] and py in self.same_vertical[d]:
                            count += self.points[(d, qy)]*self.points[(d, py)]
        return count
        
