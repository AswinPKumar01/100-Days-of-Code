class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        sum = 0

        for arr in nums:
            arr.sort()
        
        for i in range(len(nums[0])):
            highest = 0
            for j in range(len(nums)):
                highest = max(nums[j][i], highest)
            sum += highest
        
        return sum
