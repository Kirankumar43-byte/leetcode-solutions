class Solution:
    def reverse(self, x: int) -> int:
        reverse=0
        y=x
        if x<0:
            x*=(-1)
        while x!=0:
            digit=x%10
            reverse=reverse*10+digit
            x=x//10
        if y<0:
            reverse *=(-1)
        if -2**31 <reverse<2**31-1:
            return reverse
        else:
            return 0    