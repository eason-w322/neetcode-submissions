from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pattern_bank = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "_" + word[i+1:]
                if pattern not in pattern_bank:
                    pattern_bank[pattern] = []
                pattern_bank[pattern].append(word)
        
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
                for i in range(len(word)):
                    pattern = word[:i] + "_" + word[i + 1:]
                    if pattern not in pattern_bank:
                        continue
                    words = pattern_bank[pattern]
                    for w in words:
                        if w in visited:
                            continue
                        visited.add(w)
                        queue.append(w)
            step += 1
        return 0




