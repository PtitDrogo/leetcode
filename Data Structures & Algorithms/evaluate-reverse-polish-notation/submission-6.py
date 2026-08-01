class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-/*'
        if len(tokens) == 1:
            return int(tokens[0])
        for s in tokens:
            stack.append(s)
            if s in operators:
                stack.pop() #we remove the operator
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                tmp = 0
                if s == '+':
                    print(f"executing {num2} + {num1}")
                    tmp = num2 + num1
                if s == '-':
                    print(f"executing {num2} - {num1}")
                    tmp = num2 - num1
                if s == '/':
                    print(f"executing {num2} // {num1}")
                    tmp = num2 / num1
                    #somehow I need to tell it to be 0 for some reason
                if s == '*':
                    print(f"executing {num2} * {num1}")
                    tmp = num2 * num1
                stack.append(tmp)
                print(tmp)
        return int(stack.pop())

