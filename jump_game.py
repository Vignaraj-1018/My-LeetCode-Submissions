nums = [1,2]
def jumpGame():
    curr_jump = nums[0]
    n = len(nums)
    if n>1:
        for j in range(1,n):
            if nums[j] == 0:
                return False
            else:
                curr_jump = j + nums[j]
                if curr_jump == len(nums) - 1:
                    return True
    if curr_jump > len(nums) - 1:
        return False
    else:
        return True
    
print(jumpGame())