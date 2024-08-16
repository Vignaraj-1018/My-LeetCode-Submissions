class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        _min, _max = arrays[0][0], arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]

            res = max(res, arr[-1] - _min, _max - arr[0])
            _min = min(_min, arr[0])
            _max = max(_max, arr[-1])

        return res