class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        results = []
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["end"] = word
        
        row = len(board)
        col = len(board[0])
        results = []
        
        def dfs(r, c, trie):
            if "end" in trie:
                results.append(trie["end"])
                del trie["end"]
                
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] == "." or board[r][c] not in trie:
                return 
            
            
            ch = board[r][c]
            board[r][c] = "."

            dfs(r + 1, c, trie[ch])
            dfs(r - 1, c, trie[ch])
            dfs(r, c + 1, trie[ch])
            dfs(r, c - 1, trie[ch])
            
            board[r][c] = ch
        
        for i in range(row):
            for j in range(col):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        return results