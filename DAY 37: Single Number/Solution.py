class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            return functools.reduce(lambda x, y: x^y,nums)
