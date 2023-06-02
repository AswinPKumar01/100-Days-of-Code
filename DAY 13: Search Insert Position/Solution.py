class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, char in enumerate(nums):
            if char >= target:
                return i
        if not nums:
            return 0
        
        return len(nums)
