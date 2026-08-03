from typing import List
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [None] * (n + 1)  
        def dfs(i: int) -> int:
            if i == n:
                return 0
            if dp[i] is not None:
                return dp[i]

            total, best = 0, float('-inf')
            for x in range(1, 4):
                if i + x <= n:
                    total += stoneValue[i + x - 1]
                    best = max(best, total - dfs(i + x))
            dp[i] = best
            return best

        result = dfs(0)
        if result > 0:
            return "Alice"
        elif result < 0:
            return "Bob"
        else:
            return "Tie"
