class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        sum_moves = 0
        right_ones = 0
        
        for i in range(n):
            if boxes[i] == '1':
                sum_moves += i
                right_ones += 1
        
        res = [0] * n
        prefix_sum = 0
        left_ones = 0
        
        for i in range(n):
            moves = sum_moves + prefix_sum
            res[i] = moves
            
            if boxes[i] == '1':
                left_ones += 1
                right_ones -= 1
            prefix_sum += left_ones
            sum_moves -= right_ones
        
        return res