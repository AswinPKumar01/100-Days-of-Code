class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high,curr = 0,0

        for i in  gain:
            curr += i
            high = max(high, curr)

        return high
