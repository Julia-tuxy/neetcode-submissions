class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'}':'{',']':'[',')':'('}
        stack = []

        for c in s:
            if c not in parentheses:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif stack[-1] != parentheses[c]:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False
        
        return True