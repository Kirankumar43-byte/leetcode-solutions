class Solution:
    def isMatch(self, s, p):
        return bool(re.fullmatch(p, s))
        return re.fullmatch(p, s)