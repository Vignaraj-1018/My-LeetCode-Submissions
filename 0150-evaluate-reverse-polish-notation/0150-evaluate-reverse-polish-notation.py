class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tk in tokens:
            if tk =="+":
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif tk =="-":
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif tk =="*":
                stack.append(stack.pop(-2) * stack.pop(-1))
            elif tk =="/":
                stack.append(int(stack.pop(-2) / stack.pop(-1)))
            else:
                stack.append(int(tk))
                
        return stack[0]