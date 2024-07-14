class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[i_start:i] or 1)
                for elem, cnt in top.items():
                    stack[-1][elem] += cnt * multiplier
            else:
                i_start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                elem = formula[i_start:i]
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                cnt = int(formula[i_start:i] or 1)
                stack[-1][elem] += cnt

        element_count = stack[0]
        
        res = ''
        
        for ele in sorted(element_count):
            count = "" if element_count[ele] == 1 else str(element_count[ele])
            res += ele + count

        return res