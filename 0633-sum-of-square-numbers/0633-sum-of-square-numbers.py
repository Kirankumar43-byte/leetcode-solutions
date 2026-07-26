class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:  
            b2 = c - a * a
            b = int(b2 ** 0.5) 
            if b * b == b2:
                return True
            a += 1
        return False