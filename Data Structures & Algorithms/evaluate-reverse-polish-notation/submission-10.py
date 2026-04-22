class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: int(a + b),
            "-": lambda a, b: int( a - b),
            "*": lambda a, b: int(a * b),
            "/": lambda a, b: int(a / b)
            }
        for c in tokens:
            if c in ops:
                second_digit = stack.pop()
                first_digit = stack.pop()
                stack.append(ops[c](first_digit, second_digit))
            else:
                stack.append(int(c))
        return stack.pop()        
        
        