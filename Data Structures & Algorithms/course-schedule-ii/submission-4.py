class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list)
        for course, pre in prerequisites:
            courses[course].append(pre)
        
        results = []
        visiting = set()
        done_visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in done_visiting:
                return True
            visiting.add(course)
            for pre in courses[course]:
                if not dfs(pre):
                    return False
            done_visiting.add(course)
            results.append(course)
            visiting.discard(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return results
        
