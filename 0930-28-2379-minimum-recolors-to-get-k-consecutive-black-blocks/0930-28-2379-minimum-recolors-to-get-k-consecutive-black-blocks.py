class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, rclr = 0, 0
        res = k

        for r in range(len(blocks)):
            if blocks[r] == "W":
                rclr += 1
            
            if r - l + 1 == k:
                res = min(res, rclr)
                if blocks[l] == "W":
                    rclr -= 1
                l += 1
        
        return res