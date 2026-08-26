from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        patterns = {}
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                pat = word[:i]+"_"+ word[i+1:]
                if pat not in patterns:
                    patterns[pat] = []
                patterns[pat].append(word)
        
        queue = deque([beginWord])
        step = 1
        visited = set()
        visited.add(beginWord)

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return step
                for i in range(L):
                    pat = word[:i] + "_" + word[i+1:]
                    for match in patterns.get(pat, []):
                        if match not in visited:
                            visited.add(match)
                            queue.append(match)
            step += 1
        
        return 0
        



