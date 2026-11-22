class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new = ""
            for i in range(0, len(s), k):
                group = s[i:i+k]
                new += str(sum(int(c) for c in group))
            s = new
        return s