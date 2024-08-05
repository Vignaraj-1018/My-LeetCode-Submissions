class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = defaultdict(int)
        for s in arr:
            counter[s] += 1
        for i in counter:
            if counter[i] == 1:
                k -= 1
                if k == 0:
                    return i
        return ''
