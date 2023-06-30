class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        idx = [-1] * 128
        left = 0
        
        for right in range(n):
            if idx[ord(s[right])] >= left:
                left = idx[ord(s[right])] + 1
            idx[ord(s[right])] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
