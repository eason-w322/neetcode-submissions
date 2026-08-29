import heapq
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                graph[c] = set()

        indegree = {}
        for c in graph:
            indegree[c] = 0
        
        for i in range(len(words) - 1):
            j = i + 1
            word1 = words[i]
            word2 = words[j]
            min_length = min(len(word1), len(word2))
            difference_found = False
            for k in range(min_length):
                if word1[k] != word2[k]:
                    if word2[k] not in graph[word1[k]]:
                        graph[word1[k]].add(word2[k])
                        indegree[word2[k]] += 1
                    difference_found = True
                    break
            if len(word1) > len(word2) and not difference_found:
                return ""
        
        min_heap = [c for c in indegree if indegree[c] == 0]
        heapq.heapify(min_heap)
        results = []
        
        while min_heap:
            c = heapq.heappop(min_heap)
            results.append(c)
            for decendants in graph[c]:
                indegree[decendants] -= 1
                if indegree[decendants] == 0:
                    heapq.heappush(min_heap, decendants)
        
        if len(results) != len(graph):
            return ""
        return "".join(results)

                

        

                