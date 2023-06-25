class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        space = text.count(" ")
        words = text.split()
        length = len(words)

        if length-1>0:
            r = space//(length-1)
        else:
            r = space
        
        a = ""

        for i in words:
            a = a+i

            if space >= r:
                a = a+" "*r
                space -= r

        if space > 0:
            a=a+" "*space

        return a
            
