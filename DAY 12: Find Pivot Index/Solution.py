class Solution(object):
    def pivotIndex(self, nums):
      
        leftSum, rightSum = 0, sum(nums)
        for index, char in enumerate(nums):
            rightSum -= char
            if leftSum == rightSum:
                return index     
            leftSum += char
        return -1   
