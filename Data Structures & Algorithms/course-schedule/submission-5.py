class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for i, j in prerequisites:
            courses[i].append(j)
        visiting = set()
        done = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in done:
                return True
            visiting.add(course)
            for pre in courses[course]:
                if not dfs(pre):
                    return False
            
            done.add(course)
            visiting.discard(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        

        
