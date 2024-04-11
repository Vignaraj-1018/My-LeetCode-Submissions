class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def brackTrack(openN, closeN):

            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN< n:
                stack.append("(")
                brackTrack(openN+1,closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                brackTrack(openN,closeN+1)
                stack.pop()
            
        brackTrack(0,0)
        return res