class Solution:
    def longestSubarray(self, nums):
        zero = 1
        l, r  = 0, 0

        for r in range(len(nums)):
            zero -= nums[r] == 0
            if zero < 0:
               zero += nums[l] == 0
               l+= 1

        return r - l
