class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        sig=-1 if s[0]=='-' else 1
        if s[0] in ['-','+']:
            s=s[1:]
        num=0
        for i in s:
            if not i.isdigit():
                break
            num=num*10+int(i)
        num*=sig
        return max(-2**31,min(num,2**31-1))
        