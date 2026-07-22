class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}','[':']'}
        m = []
        for x in s:
            if x in d:
                m.append(x)
            else: 
                if len(m) and d[m[-1]] == x:
                    del m[-1]
                else:
                    return False
        return not m