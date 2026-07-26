class Solution:
    def selfDividingNumbers(self, l: int, r: int) -> List[int]:
        c=[]
        for i in range(l,r+1):
            for j in str(i):
                if int(j)==0 or i%int(j)!=0:
                    break
            else:
                c.append(i)
        return c
                    