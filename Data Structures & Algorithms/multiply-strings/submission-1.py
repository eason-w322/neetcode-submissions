class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)

        number_1 = 0
        for i in range(m):
            number_1 = number_1 * 10 + int(num1[i])
        
        number_2 = 0
        for j in range(n):
            number_2 = number_2 * 10 + int(num2[j])
        
        return str(number_1 * number_2)


        