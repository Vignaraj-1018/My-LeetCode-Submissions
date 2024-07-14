class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_formula(formula):
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
            return stack[0]

        element_count = parse_formula(formula)
        
        res = ''
        for ele in sorted(element_count):
            res += ele
            if element_count[ele] > 1:
                res += str(element_count[ele])
        return res