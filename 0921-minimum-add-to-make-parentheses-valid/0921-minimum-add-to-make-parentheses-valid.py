class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        # res = 0
        for c in s:
            stack.append(c)
            if len(stack) >= 2 and stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
            
        return len(stack)
            