class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandies = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                candies[i] = True
            else:
                candies[i] = False
        return candies