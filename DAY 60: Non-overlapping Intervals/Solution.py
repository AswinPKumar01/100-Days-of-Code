class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result, prev = 0, -sys.maxsize
        for l, r in intervals:
            if l < prev:
                result += 1
                if r > prev:
                    continue
            prev = r
        return result
