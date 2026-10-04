class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(range(n), key = lambda x : position[x], reverse = True)
        stack = []
        for c in cars:
            time = (target - position[c]) / speed[c]
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)