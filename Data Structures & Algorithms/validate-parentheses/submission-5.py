class Solution:
    def isValid(self, s: str) -> bool:
        parans = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        stack = []

        for ch in s:
            if ch in ('(','[','{'):
                stack.append(ch)
            elif len(stack) > 0 and parans[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
