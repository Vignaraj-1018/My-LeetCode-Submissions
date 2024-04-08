class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack and closeToOpen[ch] == stack.pop():
                    continue
                else:
                    return False

        return len(stack) == 0