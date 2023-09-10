class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        y=set(nums)
        m=list(y)

        if len(y)==1:
            return m[0]

        elif len(y)==2:
            m.sort()
            return m[-1]

        else:
            for i in range(3):
                for j in range(len(m)-1):
                    if m[j]>m[j+1]:
                        m[j],m[j+1]=m[j+1],m[j]

            return m[-3]
