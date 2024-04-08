class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                cur = stack.pop()
                if (ch == ")" and cur == "(") or (ch == "]" and cur == "[") or (ch == "}" and cur == "{"):
                    continue
                else:
                    return False

        return len(stack) == 0