class Solution:
    def rob(self, nums: List[int]) -> int:
        curr, end = 0, 0

        for i in nums:
            end, curr = curr, max(end + i, curr)
            
        return curr
