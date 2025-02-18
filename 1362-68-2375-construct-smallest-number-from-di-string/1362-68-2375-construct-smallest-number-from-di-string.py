class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        st = []
        res = []

        for i in range(1, n + 2):
            st.append(i)
            if i == n + 1 or pattern[i - 1] == 'I':
                while st:
                    res.append(str(st.pop()))

        return ''.join(res)