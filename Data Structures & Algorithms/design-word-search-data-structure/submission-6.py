class WordDictionary:

    def __init__(self):
        self.wordDict = {}
        

    def addWord(self, word: str) -> None:
        d = self.wordDict
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["end"] = True
        

    def search(self, word: str) -> bool:

        def dfs(d, index):
            if index == len(word):
                return "end" in d
            if word[index] in d:
                d = d[word[index]]
                return dfs(d, index + 1)
            elif word[index] == ".":
                return any(dfs(d[key], index+1) for key in d if key != "end")
            else:
                return False

        return dfs(self.wordDict, 0)
    
                
                    

