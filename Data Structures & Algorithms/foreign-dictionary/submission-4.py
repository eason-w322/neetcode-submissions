import heapq
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
        
        indegree = {}
        for c in graph:
            indegree[c] = 0
        
        for i in range(len(words)-1):
            j = i + 1
            word1 = words[i]
            word2 = words[j]
            min_length = min(len(word1), len(word2))
            found = False
            for k in range(min_length):
                if word1[k] != word2[k]:
                    if word2[k] not in graph[word1[k]]:
                        graph[word1[k]].add(word2[k])
                        indegree[word2[k]] += 1
                    found = True
                    break
            if len(word1) > len(word2) and not found:
                return ""
            
        min_heap = [c for c in indegree if indegree[c] == 0]
        results = []
        while min_heap:
            c = heapq.heappop(min_heap)
            results.append(c)
            for decendant in graph[c]:
                indegree[decendant] -= 1
                if indegree[decendant] == 0:
                    heapq.heappush(min_heap, decendant)
        if len(results) != len(graph):
            return ""
        return "".join(results)
            


        

                