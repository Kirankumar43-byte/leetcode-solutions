class Solution:
    def validSequence(self, s1: str, s2: str) -> list[int]:
        n = len(s1)
        m = len(s2)
        res = []
        dp = [0] * (n + 1)
        op = True
        cur = m - 1
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            if cur >= 0 and s1[i] == s2[cur]:
                cur -= 1
                dp[i] += 1
        j = 0 
        for i in range(n):
            if j >= m:
                break
            if s1[i] == s2[j]:
                res.append(i)
                j += 1
            elif dp[i + 1] + 1 > m - j - 1 and op:
                res.append(i)
                op = False
                j += 1
        if len(res) != m:
            return []
        return res