class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            elif t == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif t == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif t == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif t == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a / b)

        return int(stack[-1])