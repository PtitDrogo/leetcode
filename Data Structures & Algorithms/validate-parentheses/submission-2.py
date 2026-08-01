class Solution:
    def isValid(self, s: str) -> bool:
        delim = '[{('
        delimEnv = ']})'
        stack = []
        for c in s:
            if c in delimEnv:
                if len(stack) == 0:
                    return False
                if c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
