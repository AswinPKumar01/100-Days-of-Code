class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        strs.sort()
        first, last = strs[0], strs[-1]

        for i in range(min(len(first),len(last))):
            if(first[i] != last[i]):
                return pref
            
            pref += first[i]

        return pref
        
