class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        path = path.split('/')
        
        for i in path:
            if i == '' or i=='.':
                continue
            if i == '..':
                if stack:
                    stack.pop()
                continue
            
            stack.append(i)
        return '/' + '/'.join(stack)
            