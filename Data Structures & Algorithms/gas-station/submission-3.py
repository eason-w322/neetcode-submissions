class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        start = 0
        fuel = 0
        n = len(gas)

        for i in range(n):
            fuel = fuel + gas[i % n] - cost[i % n]
            if fuel < 0:
                start = i + 1
                fuel = 0
        
        return start