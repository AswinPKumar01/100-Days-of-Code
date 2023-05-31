class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1

        for i in range(len(nums)):
            prod*=nums[i]

        if (prod == 0 ): return 0
        else: return int(prod/abs(prod))
