class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
      
        count1, count2 = Counter(word1), Counter(word2)
        a,b=sorted(count1.values()),sorted(count2.values())
        
        return count1.keys()==count2.keys() and a==b
