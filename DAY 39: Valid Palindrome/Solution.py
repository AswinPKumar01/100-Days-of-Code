class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = ''.join(ch for ch in s if ch.isalnum()).lower()
        return raw[::-1] == raw
