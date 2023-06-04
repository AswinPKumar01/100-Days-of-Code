class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        queue = [('(', 1,0)] 
        f = 0            
        l = 1            
        while f<l:
            cur = queue[f]
            if cur[1]+cur[2]==2*n:
                ans.append(cur[0])
                f+=1
                continue
                
            if cur[1] < n:
                queue.append((cur[0]+'(', cur[1]+1, cur[2]))
                l+=1
                
            if cur[2] < cur[1]:
                queue.append((cur[0]+')', cur[1], cur[2]+1))
                l+=1
            f+=1
        return ans
