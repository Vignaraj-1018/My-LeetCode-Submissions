class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles >= numExchange:
            cur = numBottles // numExchange
            ans += cur
            numBottles = numBottles % numExchange + cur
        
        return ans