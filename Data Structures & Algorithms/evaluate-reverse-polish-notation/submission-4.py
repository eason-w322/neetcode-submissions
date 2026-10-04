class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in ('+', '-', '*', '/'):
                stack.append(tok)
            else:
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                if tok == '+':
                    result = operand_1 + operand_2
                elif tok == '-':
                    result = operand_1 - operand_2
                elif tok == '*':
                    result = operand_1 * operand_2
                else:
                    result = int(operand_1 / operand_2)
                stack.append(str(result))
        
        return int(stack[0])