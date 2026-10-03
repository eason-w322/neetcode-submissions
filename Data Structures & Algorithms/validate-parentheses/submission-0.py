from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        candidates = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                candidates.append(s[i])

            elif not candidates and (s[i] == ")" or s[i] == "}" or s[i] == "]"):
                return False
            
            elif s[i] == ")":
                if candidates.pop() != "(":
                    return False
             
            elif s[i] == "}":
                if candidates.pop() != "{":
                    return False
            
            elif s[i] == "]":
                if candidates.pop() != "[":
                    return False
        
        return len(candidates) == 0
        