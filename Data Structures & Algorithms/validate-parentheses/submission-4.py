class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for c in s:
            # print(f'c is {c}')
            if self.isOpeningChar(c):
                stack.append(c)
                continue
            if len(stack) == 0:
                # print(f"Stack len is 0 when char {c} is read")
                return False
            poppedChar = stack.pop()
            if c != chars.get(poppedChar):
                return False
        return len(stack) == 0
    
    def isOpeningChar(self, c: str) -> bool:
        return c == '(' or c == '{' or c == '['