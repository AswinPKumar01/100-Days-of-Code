class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      
        current_sum = 0
        max_sum = float("-inf")

        for i in nums:
            current_sum +=i

            if current_sum > max_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0

        return max_sum
