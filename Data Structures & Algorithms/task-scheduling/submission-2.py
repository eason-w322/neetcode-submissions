class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        jobs = {}
        
        for task in tasks:
            jobs[task] = jobs.get(task, 0) + 1
        maximum = max(jobs[i] for i in jobs)
        count = 0
        for key in jobs:
            if jobs[key] == maximum:
                count += 1
        return max((maximum - 1) * (n + 1) + count, len(tasks))