class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = 2 * k + 1
        result = [-1] * n
        
        if n < window:
            return result
        
        pref_Sum = [0] * (n + 1)
        for i in range(n):
            pref_Sum[i + 1] = pref_Sum[i] + nums[i]
        
        for i in range(k, n - k):
            result[i] = (pref_Sum[i + k + 1] - pref_Sum[i - k]) // window
        
        return result
