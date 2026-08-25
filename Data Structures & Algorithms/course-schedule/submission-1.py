class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i:[] for i in range(0, numCourses)}
        for course, pre in prerequisites:
            courses[course].append(pre)
        
        state = [0] * numCourses
        def dfs(course):
            if state[course] == 1:
                return False
            
            if state[course] == 2:
                return True
            
            state[course] = 1
            for pre in courses[course]:
                if not dfs(pre):
                    return False

            state[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
        
