class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter

        arr1=s1.split(" ")
        arr2=s2.split(" ")
        d_ = dict(Counter(arr1+arr2))
        return [x for x,v in d_.items() if v==1]
