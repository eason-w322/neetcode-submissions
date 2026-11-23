from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        length = len(beginWord)
        dictionary = defaultdict(list)
        
        for word in wordList:
            for i in range(length):
                pattern = word[:i] + "_" + word[i+1:]
                dictionary[pattern].append(word)
        
        queue = deque()
        queue.append(beginWord)
        step = 0
        visited = set()
        
        while queue:
            step += 1
            q_length = len(queue)
            for _ in range(q_length):
                word = queue.popleft()
                if word == endWord:
                    return step
                if word in visited:
                    continue
                visited.add(word)
                for i in range(length):
                    pattern = word[:i] + "_" + word[i+1:]
                    for neighbor in dictionary[pattern]:
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
        
        return 0
            

        



