from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "_" + word[i+1:]
                if pattern not in patterns:
                    patterns[pattern] = []
                patterns[pattern].append(word)
        
        queue = deque()
        queue.append(beginWord)
        seen = set()
        seen.add(beginWord)
        step = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                word = queue.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    pattern = word[:i] + "_" + word[i+1:]
                    if pattern in patterns:
                        for candidate in patterns[pattern]:
                            if candidate in seen:
                                continue
                            seen.add(candidate)
                            queue.append(candidate)
            step += 1
        return 0
        
        



