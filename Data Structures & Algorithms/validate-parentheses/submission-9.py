class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        toRemove = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for c in s:
            #We do it the other way around
            rightHalf = toRemove.get(c)
            if len(stack) and rightHalf == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
            
