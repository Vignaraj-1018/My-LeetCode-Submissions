class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for c in s:
            
            if c == ')':
                por = []
                
                while stack[-1] != '(':
                    por.append(stack.pop())
                stack.pop()
                
                stack.extend(por)
            
            else:
                stack.append(c)
                
        return "".join(stack)