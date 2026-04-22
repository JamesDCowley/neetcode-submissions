class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                n = stack.pop()
                p = stack.pop()
                stack.append(n + p)
            elif token == '-':
                p = stack.pop()
                n = stack.pop()
                stack.append(n - p)
            elif token == '/':
                p = stack.pop()
                n = stack.pop()
                stack.append(int(float(n) / p))
            elif token == '*':
                n = stack.pop()
                p = stack.pop()
                stack.append(n * p)
            else:
                stack.append(int(token))
        if stack:
            return stack[0]
        return 0


