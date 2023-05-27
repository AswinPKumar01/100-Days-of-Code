class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amt, i, j = 0, 0, len(height)-1
        
        while (i < j):
            if height[i] <= height[j]:
                a = height[i] * (j - i)
                i += 1
            else:
                a = height[j] * (j - i)
                j -= 1

            if a > max_amt: max_amt = a
        return max_amt
