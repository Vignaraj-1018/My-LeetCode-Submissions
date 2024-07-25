class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(num1, num2):

            res = []
            i, j = 0, 0
            m, n = len(num1), len(num2)
            while i < m and j < n:
                if num1[i] < num2[j]:
                    res.append(num1[i])
                    i += 1
                else:
                    res.append(num2[j])
                    j += 1
    
            while i < m:
                res.append(num1[i])
                i += 1
            
            while j < n:
                res.append(num2[j])
                j += 1
            
            return res
        
        def mergeSort(num):
            n = len(num)
            
            if n<=1:
                return num
            
            mid = n // 2

            left = mergeSort(num[:mid])
            right = mergeSort(num[mid:])

            return merge(left, right)
        
        return mergeSort(nums)