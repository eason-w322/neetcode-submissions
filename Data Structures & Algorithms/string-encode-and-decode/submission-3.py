class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encoded_string.append(str(len(s)) + "." + s) 
        return "".join(encoded_string)


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        length = len(s)
        temp = ""
        i = 0
        while i < length:
            if s[i] == ".":
                steps = int(temp)
                temp = ""
                ###for j in range(1, steps + 1):
                    ###temp += s[i + j]
                decoded_strs.append(s[i+1 : i+steps+1])
                i = i + steps + 1
                continue
            temp += s[i]
            i += 1
        return decoded_strs




