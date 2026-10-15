class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        jobs = {}
        for task in tasks:
            jobs[task] = jobs.get(task, 0) + 1
        
        min_heap = []
        for job in jobs:
            min_heap.append((-jobs[job], job))
        heapq.heapify(min_heap)
        
        time = 0
        cool_down = deque()
        while cool_down or min_heap:
            time += 1
            while cool_down and cool_down[0][2] <= time:
                remaining, job, t = cool_down.popleft()
                heapq.heappush(min_heap, (-remaining, job))
            if not min_heap:
                continue
            remaining, job = heapq.heappop(min_heap)
            remaining = -remaining
            remaining -= 1
            if remaining == 0:
                continue
            cool_down.append((remaining, job, time + n + 1))

        return time
