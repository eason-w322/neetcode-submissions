import heapq
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters = set()
        for word in words:
            for c in word:
                letters.add(c)
        graph = defaultdict(list)
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            if word1 == word2:
                continue

            length = min(len(word1), len(word2))
            j = 0
            while j < length and word1[j] == word2[j]:
                j += 1
            if j < length:
                graph[word2[j]].append(word1[j])
                ###if word2[j] in graph[word1[j]]:
                    ###return ""
                continue
            if len(word1) > len(word2):
                return ""
        visiting = set()
        visited = set()
        results = []
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            results.append(node)
            visiting.discard(node)
            visited.add(node)
            return True
        
        for c in letters:
            if not dfs(c):
                return ""
        
        return "".join(results)
        

            


            
            





        

                