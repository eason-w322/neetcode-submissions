from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        pattern = {}
        for word in wordList:
            for i in range(n):
                pat = word[:i] + "_" + word[i + 1:]
                if pat not in pattern:
                    pattern[pat] = []
                pattern[pat].append(word)
        
        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)

        step = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                word = queue.popleft()
                if word == endWord:
                    return step
            
                for i in range(n):
                    match = word[:i] + "_" + word[i+1:]
                    words = pattern.get(match, [])
                    for w in words:
                        if w in visited:
                            continue
                        visited.add(w)
                        queue.append(w)
            step += 1
        return 0
        



