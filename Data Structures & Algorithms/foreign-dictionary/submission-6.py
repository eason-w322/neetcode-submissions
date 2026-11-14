import heapq
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dependency = defaultdict(list)
        letters = set(c for word in words for c in word)
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            j = 0
            if word1 == word2:
                continue
            length = min(len(word1), len(word2))
            while j < length - 1 and word1[j] == word2[j]:
                j += 1
            if word1[j] != word2[j]:
                dependency[word2[j]].append(word1[j])
                if word2[j] in dependency[word1[j]]:  ### complexity O(n)
                    return ""
                continue
            if  len(word1) > len(word2):
                return ""
            else:
                continue

        results = []
        visited = set()
        visiting = set()
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for neighbor in dependency[node]:
                    if not dfs(neighbor):
                        return False
            results.append(node)
            visited.add(node)
            visiting.remove(node)
            return True
            
        
        for c in letters:
            if not dfs(c):
                return ""
        
        return "".join(results)



        






        

                